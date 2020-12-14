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

  const [newsResult, setNewsResult] = useState({
    news_pred_result: '',
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
    }, 500);

    get_news_pred_result()
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

  const get_news_pred_result = async () => {
    let filtered = []
    let posneg = ""
    await axios.get("http://localhost:3001/news_pred_result")
      .then(res => {
        filtered = res.data.filter(data => data.code === props.code)
        if(filtered[0].news_pred === "긍정") {
          posneg = "매수"
        } else if(filtered[0].news_pred === "부정") {
          posneg = "매도"
        }
        setNewsResult({
          news_pred_result: posneg,
        })
      })
  }

  return (
    <>
      <table border="0" width="100%" height="500px">
          <tr>
            <td rowSpan="2" width="60%">{loadingState.loading === true ? <CircularProgress className="spinner" /> : <Chart data={objStock.data} />}</td>
            <td>
              {props.code}.KS종목 {newsResult.news_pred_result} 추천!
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
