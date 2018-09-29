#!/usr/bin/env python
import os
import menlooker
from threading import Lock
from flask import Flask, render_template, session, request, url_for
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from flask import send_from_directory

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = 'eventlet'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

@app.route('/js/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join('.' 'static', 'js'), filename)


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    # while True:
    #     socketio.sleep(10)
    #     count += 1
    #     print(".............background_thread")
    #     _data = menlooker.get_men("com.meizu.media.music")
    #     socketio.emit('pong',{"c_time":_data[0], "data":_data[1]},
    #                   namespace='/test')
        # socketio.emit('pong',
        #               {'data': 'Server generated event', 'count': count},
        #               namespace='/test')


@app.route('/')
def index():
    return render_template('indexx.html',async_mode=socketio.async_mode)

# @app.route('/static/js/<path:path>')
# def send_js(path):
#     return app.send_static_file(os.path.join('js', path).replace('\\','/'))

class MyNamespace(Namespace):
    def on_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': "in_event", 'count': session['receive_count']})

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    # def on_sping(self, msg):
    # 	print("spinging..............")
    # 	_data = menlooker.get_men("com.meizu.media.music")
    # 	emit('spong',{"pre_time": msg['time'], "c_time":_data[0], "data":_data[1]})
    def on_sping(self, msg):
    	_data = menlooker.get_men("com.meizu.media.music")
    	emit('spong', {'pre_time': msg['time'], 'c_time': _data[0], 'c_value' : _data[1]})
    	pass

    def on_connect(self):
        # global thread
        # with thread_lock:
        #     if thread is None:
                # thread = socketio.start_background_task(
                #     target=background_thread)
        emit('my_response', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)


socketio.on_namespace(MyNamespace('/test'))


if __name__ == '__main__':
    socketio.run(app, debug=True)
