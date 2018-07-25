#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# to use websocket , we need to install Flask-SocketIO best(can use pip to install)
# about Flask-SocketIO ,can see https://github.com/miguelgrinberg/Flask-SocketIO
# @time  2018-7-25 13:31:44
# @athor asange
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route(r'//Mzkj-pc-00131/Users/liyixi/Desktop/1891VCC')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app)