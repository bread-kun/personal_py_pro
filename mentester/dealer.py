#!/usr/bin/env python
import os
import menlooker
from threading import Lock
from flask import Flask, render_template, session, request, url_for
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = 'threading'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@app.route('/')
def index():
    statics_socket_io = url_for("static", filename="js/socket.io-1.4.5.js")
    statics_echart_op = url_for("static", filename="js/option.js")
    return render_template('index.html',socket_io = statics_socket_io,echart_op = statics_echart_op, async_mode=socketio.async_mode)
    # return render_template('index.html',async_mode=socketio.async_mode)

@app.route('/static/js/<path:path>')
def send_js(path):
    return app.send_static_file(os.path.join('js', path).replace('\\','/'))

class MyNamespace(Namespace):
    def on_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']})

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    def on_ping(self):
        _data = menlooker.get_men("com.meizu.media.music")
        emit('pong',{"c_time":_data[0], "data":_data[1]})

    def on_connect(self):
        global thread
        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(
                    target=background_thread)
        emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)


socketio.on_namespace(MyNamespace('/test'))


if __name__ == '__main__':
    socketio.run(app, debug=True)
