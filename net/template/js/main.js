$(document).ready(function () {
	var host = "http:http://127.0.0.1:5000/";
	var socket = io.connect(host);

	socket.on('connect', function (message) {
		console.log("connect message:" + message)
		let time = new Date();
		let _data = {
			"info" : "client is connect",
			"time" : time,
			"detail_time" : time.getTime()
		};
		socket.emit('log',{data: _data})
	})

	var ping_queue = [];
	var interval = window.setInterval(function () {
		var start_time = (new Date).getTime();
		ping_queue.push(start_time);
		socket.emit('client_ping');
	}, 1000);

	socket.on('pong', function () {
		if (ping_queue.length()>0) {
			let start_time = ping_queue.shift();
			let communite_time = (new Date).getTime() - start_time;
			console.log("communite time:" + communite_time)
		}
	})

	$("#send-form>:button").onclick(function () {
		var commond = $("#m").val();
		let _data = {
			"commond" : commond
		};
		socket.emit('commond', {data: _data})
	})

	function printMessage(msg) {
		// body...
	}
})