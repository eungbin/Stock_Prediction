import React, { useEffect, useState } from 'react';
import Highcharts from "highcharts";
import HighchartsReact from "highcharts-react-official";
import { Chart } from "react-google-charts";

function chart(props) {
    const [ chartState, setChartState ] = useState({
        date: [],
        price: [],
    })
    
    useEffect(() =>  {
        setChartState({
            date: props.date,
            price: props.close,
        })
    }, [props]);
    // const series2 = props.close;    //App.js에서 데이터를 보내줄 예정
    // const date = props.date;
    // const options = {
    //     chart: {
    //         type: 'line'		// line 차트. 아무 설정이 없으면 line chart가 된다.
    //     },
    //     title: {
    //         text: '종가 기준 주가 그래프'
    //     },
    //     credits: {
    //         enabled: false
    //     },
    //     // xAxis: {
    //     //     type: 'datetime',
    //     //     dateTimeLabelFormats: {
    //     //         "day": date
    //     //     },
    //     // },
    //     xAxis: { 
    //         type: 'category',
    //     },
    //     legend: {
    //         reversed: true
    //     },
    //     plotOptions: {
    //         series: {
    //             stacking: 'normal',
    //             dataLabels: {
    //                 enabled: false,
    //                 format: "<b>{point.y}</b>",
    //             }
    //         }
    //     },
    //     series: [{ name: "data", data: series2 }]
    // }
    return (
        <>
            {/* <HighchartsReact highcharts={Highcharts} options={options} /> */}
            <Chart
                chartType="LineChart"
                data={[["Date", "Price"], chartState.date, chartState.price]}
                width="600px"
                height="400px"
                legendToggle
            />
        </>
    );
}

export default chart;
