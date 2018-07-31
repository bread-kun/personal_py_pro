#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# to use websocket , we need to install Flask-SocketIO best(can use pip to install)
# if have no install eventlet nor gevent, it will ont support the websocket
# about Flask-SocketIO ,can see https://github.com/miguelgrinberg/Flask-SocketIO
# @time  2018-7-25 13:31:44
# @athor asange
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

# dont need json support ,because when you recive the param message, that are diet all ready
# import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('log')
def handle_connect(message):
	# _json_data = json.dumps(message)
	print('connect with message :',message)
	# print(type(message))
	# emit('my_response', {'data': "you are connected"})
	pass

@socketio.on('client_ping')
def handle_comunicate(message):
	emit('pong')
	print('client_ping-------',message['time'])
	pass

@socketio.on('commond')
def test_message(message):
    import json
    print('received message:' + message['data']['commond'])
    _lt = time.localtime()
    _test_diet = {
    	"time":"{0}-{1:0>2d}-{2:0>2d} {3:0>2d}:{4:0>2d}:{5:0>2d}".format(_lt[0],_lt[1],_lt[2],_lt[3],_lt[4],_lt[5]),
    	"int_t": 66,
    	"float_t": 66.89,
    	"array_t": [12,35,68,78,96],
    	"string": "this string content nothing"
    	}
    # maybe you need deal some object wite object function __str__() to switch to string type
    emit('my_response', json.dumps(_test_diet))

@socketio.on('client_leave')
def handle_disconnect(message):
	print('disconnect with message:', str(message))
	pass

@socketio.on("__commond")
def handle_commond(message):
	# __json_data = json.dumps(message)
	print('get by commond:', __json_data['commond'])
	pass

@socketio.on("json")
def handle_json(json):
	# print('received json:' + str(json))
	pass

if __name__ == '__main__':
    socketio.run(app)