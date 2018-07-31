$(document).ready(function () {
	var host = "http://127.0.0.1:5000/";
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
/*	var interval = window.setInterval(function () {
		let start_time = (new Date).getTime();
		ping_queue.push(start_time);
		socket.emit('client_ping',{time: start_time});
	}, 1000);
*/
	socket.on('pong', function () {
		if (ping_queue.length>0) {
			let start_time = ping_queue.shift();
			let communite_time = (new Date).getTime() - start_time;
			console.log("communite time:" + communite_time)
		}
	})

	$("#send-form>:button").click(function (event) {
		var commond = $("#m").val();
		if (commond === "#leave") {
			window.clearInterval(interval);
			socket.on("disconnect", function(){
				socket.emit('disconnect', {data: "i;m disconnecting"})
			})
		}
		let _data = {
			"commond" : commond
		};
		socket.emit('commond', {data: _data})
		// stop submit
		return false;
	})
	function printMessage(msg) {
		// body...
		alert(msg)
	}
	window.onload = function () {
		alert("page refresh")
	}
})