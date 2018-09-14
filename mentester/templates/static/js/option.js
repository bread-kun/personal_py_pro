var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
option = null;
function setData(ctime,val) {
    return {
        name: ctime,
        value: val
    }
}
option = {
    title: {
        text: '动态数据 + 时间坐标轴'
    },
    tooltip: {
        trigger: 'axis',
        formatter: function (params) {
            params = params[0];
            return params.name + ' : ' + params.value;
        },
        axisPointer: {
            animation: false
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

//     for (var i = 0; i < 5; i++) {
//         data.shift();
//         data.push(randomData());
//     }

//     myChart.setOption({
//         series: [{
//             data: data
//         }]
//     });
// }, 1000);;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}