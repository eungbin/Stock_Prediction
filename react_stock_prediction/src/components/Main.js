import React, { useEffect, useState } from 'react';
import './../css/Main.css';
import { makeStyles } from '@material-ui/core/styles';
import Chart from './chart';
import axios from 'axios';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

function Main(props) {
  const [stockState, setStockState] = useState({
    close: [],
    date: [],
  })
  useEffect(() =>  {
    axios.get("http://localhost:3001/data", {
        params: {
          code: props.code,
        }
      })
      .then(res => {
        let arr_date = []
        let arr_close = []
        res.data.map(data => {
          arr_date.push(data.date)
          arr_close.push(data.close)
        })
        setStockState({
          close: arr_close,
          date: arr_date,
        })
      })
  }, []);

  const test_state = () => {
    console.log(props.code)
  }

  const classes = useStyles();
  return (
    <>
      <table border="1" width="100%" height="500px">
          <tr>
            <td rowSpan="2" width="60%"><Chart date={stockState.date} close={stockState.close}/></td>
            <td>d</td>
          </tr>

          <tr>
            <td><button onClick={test_state}>Test</button></td>
          </tr>
      </table>
    </>
  );
}

export default Main;
