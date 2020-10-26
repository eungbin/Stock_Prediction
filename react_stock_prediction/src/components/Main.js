import React, { useEffect, useState } from 'react';
import './../css/Main.css';
import { makeStyles } from '@material-ui/core/styles';
import Chart from './chart';

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
  const test_state = () => {
    console.log(props.close)
  }

  const classes = useStyles();
  return (
    <>
      <table border="1" width="100%" height="500px">
          <tr>
            <td rowSpan="2" width="60%"><Chart date={props.date} close={props.close}/></td>
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
