import React, { useEffect, useState } from 'react';
import './App.css';
import Main from './components/Main';
import Header from './components/Header';
import axios from 'axios';

function App() {
  const [testState, setTestState] = useState({
    high: [],
  })
  useEffect(() =>  {
    axios.get("http://localhost:3001/data")
      .then(res => {
        console.log(res.data)
        setTestState({
          high: res.data
        })
      })
    
      console.log("test")
      console.log(testState)
  }, []);

  const test_state = () => {
    console.log(testState.high)
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
        <Main />
        <button onClick={test_state}>Test</button>
      </div>
    </div>
  );
}

export default App;
