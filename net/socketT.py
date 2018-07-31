#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# to use websocket , we need to install Flask-SocketIO best(can use pip to install)
# if have no install eventlet nor gevent, it will ont support the websocket
# about Flask-SocketIO ,can see https://github.com/miguelgrinberg/Flask-SocketIO
# @time  2018-7-25 13:31:44
# @athor asange
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('log')
def handle_connect(message):
	print('connect with message :',str(message))
	# emit('my_response', {'data': "you are connected"})
	pass

@socketio.on('client_ping')
def handle_comunicate():
	emit('pong')
	pass

@socketio.on('message')
def test_message(message):
    print('received message:' + message['data'])
    emit('my_response', {'data': 'got it!'})

@socketio.on("json")
def handle_json(json):
	print('received json:' + str(json))
	pass

if __name__ == '__main__':
    socketio.run(app)