import React, { useEffect, useState } from 'react';
import moment from "moment";
import {
    AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip,
  } from 'recharts';

function Showchart(props) {
    const [ chartData, setChartData ] = useState({
        data: [],
    })
    useEffect(() =>  {
        let modify = props.data
        let i = 0

        modify.map(data => {
            data.date = moment(data.date).format('YYYY-MM-DD')
            modify[i].date = data.date
            i  = i + 1
        })

        setChartData({
            data: modify,
          })
      }, [props]);
      return (
        <AreaChart
          width={900}
          height={400}
          data={chartData.data}
          margin={{
            top: 10, right: 30, left: 0, bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Area type="monotone" dataKey="close" stroke="#8884d8" fill="#ffffff" />
        </AreaChart>
      );
}

export default Showchart;
