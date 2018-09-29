var data = [];
    $(document).ready(function() {
        namespace = 'test';
        var start_flag = false;
        var socket = io.connect("http://127.0.0.1:5000/" + namespace);
        socket.on('connect', function() {
            console.log("connected");
            start_flag = true;
        });
        socket.on('my_response', function(msg) {
            $('#log').append('<br>' + $('<div/>').text('Received #' + msg.count + ': ' + msg.data).html());
        });
        var ping_pong_times = [];
        var start_time;
        window.setInterval(function() {
            start_time = (new Date).getTime();
            socket.emit('ping');
        }, 1000);
        socket.on('pong', function(msg) {
            var latency = (new Date).getTime() - start_time;
            ping_pong_times.push(latency);
            ping_pong_times = ping_pong_times.slice(-30); // keep last 30 samples
            var sum = 0;
            for (var i = 0; i < ping_pong_times.length; i++)
                sum += ping_pong_times[i];
            $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);


            ///////////////////////////////////
            data.push(setData(msg.c_time,msg.data))
            myChart.setOption(option);
            ///////////////////////////////////
        });
        $('form#emit').submit(function(event) {
            socket.emit('my_event', {data: $('#emit_data').val()});
            return false;
        });
        $('form#disconnect').submit(function(event) {
            socket.emit('disconnect_request');
            return false;
        });
    });

// var dom = document.getElementById("container");
// var myChart = echarts.init(dom);
// var app = {};
// option = null;
// function setData(ctime,val) {
//     return {
//         name: ctime,
//         value: val
//     }
// }
// option = {
//     title: {
//         text: '动态数据 + 时间坐标轴'
//     },
//     tooltip: {
//         trigger: 'axis',
//         formatter: function (params) {
//             params = params[0];
//             return params.name + ' : ' + params.value;
//         },
//         axisPointer: {
//             animation: false
//         }
//     },
//     xAxis: {
//         type: 'time',
//         splitLine: {
//             show: false
//         }
//     },
//     yAxis: {
//         type: 'value',
//         boundaryGap: [0, '100%'],
//         splitLine: {
//             show: false
//         }
//     },
//     series: [{
//         name: '模拟数据',
//         type: 'line',
//         showSymbol: false,
//         hoverAnimation: false,
//         data: data
//     }]
// };

// // setInterval(function () {

// //     for (var i = 0; i < 5; i++) {
// //         data.shift();
// //         data.push(randomData());
// //     }

// //     myChart.setOption({
// //         series: [{
// //             data: data
// //         }]
// //     });
// // }, 1000);;
// if (option && typeof option === "object") {
//     myChart.setOption(option, true);
// }

var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
var data = [];
option = null;
function randomData() {
    d = new Date();
    _value = 3000 + Math.floor(Math.random()*500) - 250;
    console.log(d,_value);
    return {
        name: d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds(),
        value: [d,_value]
    }
}

function setData(ctime,val) {
    return {
        name: ctime,
        value: [ctime,val]
    }
}

var oneDay = 24 * 3600 * 1000;
// var value = Math.random() * 1000;
for (var i = 0; i < 1000; i++) {
    re = randomData();
    console.log(re);
    data.push(re);
}

option = {
    title: {
        text: '左上角的标题'
    },
    tooltip: {
        trigger: 'axis',
        formatter: function (params) {
            console.log("---->",params);
            return params[0].name + ' :  ' + params[0].value[1];
        },
        axisPointer: {
            animation: true
        }
    },
    xAxis: {
        type: 'time',
        splitLine: {
            show: false
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%'],
        splitLine: {
            show: false
        }
    },
    series: [{
        name: '模拟数据',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: data
    }]
};

// setInterval(function () {

//     data.shift();
//     data.push(randomData());
//     myChart.clear();
    myChart.setOption(option);
// }, 1000);
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}