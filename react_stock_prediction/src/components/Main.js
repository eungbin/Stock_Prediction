import React, { useEffect, useState } from 'react';
import './../css/Main.css';
import Chart from './chart';
import axios from 'axios';
import { CircularProgress } from '@material-ui/core';

function Main(props) {
  const [objStock, setObjStock] = useState({
    data: [],
  })

  const [loadingState, setLoadingState] = useState({
    loading: true,
  })

  useEffect(() =>  {
    setLoadingState({
      loading: true,
    })

    axios.get("http://localhost:3001/data", {
        params: {
          code: props.code,
        }
      })
      .then(res => {
        setObjStock({
          data: res.data,
        })
      })
    
    setTimeout(function() {
      setLoadingState({
        loading: false,
      })
    }, 1500);
  }, []);

  // const get_pred_result = () => {
  //   let filtered = []
  //   axios.get("http://localhost:3001/pred_result")
  //     .then(res => {
  //       filtered = res.data.filter(data => data.code === props.code)
  //       console.log(filtered[0].pred)
  //       return filtered[0].pred
  //     })
  // }

  return (
    <>
      <table border="0" width="100%" height="500px">
          <tr>
            <td rowSpan="2" width="60%">{loadingState.loading === true ? <CircularProgress className="spinner" /> : <Chart data={objStock.data} />}</td>
            <td>
            </td>
          </tr>

          <tr>
            <td>
            </td>
          </tr>
      </table>
    </>
  );
}

export default Main;
