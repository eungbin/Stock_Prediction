import React, { useEffect, useState } from 'react';
import './App.css';
import Main from './components/Main';
import Header from './components/Header';
import axios from 'axios';

function App() {
  const [testState, setTestState] = useState({
    close: [],
    date: [],
  })
  useEffect(() =>  {
    axios.get("http://localhost:3001/data")
      .then(res => {
        let arr_date = []
        let arr_close = []
        console.log(res.data)
        console.log(res.data[0].date)
        res.data.map(data => {
          arr_date.push(data.date)
          arr_close.push(data.close)
        })
        setTestState({
          close: arr_close,
          date: arr_date,
        })
      })
  }, []);

  const test_state = () => {
    console.log(testState.close)
  }

  const get_pred_result = () => {
    axios.get("http://localhost:3001/pred_result")
      .then(res => {
        console.log(res.data)
      })
  }

  return (
    <div className="mapWrapper">
      <div className="App-Header">
        <Header />
      </div>
      <div className="App-Body">
        <Main date={testState.date} close={testState.close}/>
        <button onClick={test_state}>Test</button>
      </div>
    </div>
  );
}

export default App;
