import React, { useEffect, useState } from 'react';
import './App.css';
import Main from './components/Main';
import Header from './components/Header';
import axios from 'axios';
import Request from './components/Board/RequestBoard';
import Change from './components/Change/ChangeItem';
import Detail from './components/Board/DetailBoard';
import Register from './components/Auth/Register';
import Login from './components/Auth/Login';
import Writepage from './components/Board/WriteBoard';
import { Button } from '@material-ui/core';

function App() {
  const [codeState, setCodeState] = useState({
    code: '005930',
  })

  const [pageState, setPageState] = useState({
    page: 'Main',
  })

  const [boardState, setBoardState] = useState({
    board: {},
  })

  const [userState, setUserState] = useState({
    id: '',
    password: '',
    loginStat: sessionStorage.loginStat,
  })

  const [writeState, setWriteState] = useState({
    state: '',
  })

  const [predResult, setPredResult] = useState({
    pred_result: 0,
  })

  useEffect(() =>  {

  }, []);

  const onHeaderSubmit = async (header, loginStat) => {
    await setUserState({
      loginStat: loginStat,
    })

    await setPageState({
      page: header,
    })

    if(header === "Request") {
      setBoardState({
        board: {},
      })
    }
  };

  const onRequestBoardSubmit = async (board) => {
    await setPageState({
      page: "DetailBoard",
    })
    
    await setBoardState({
      board: board,
    })
  }

  const goWriteBoardSubmit = async () => {
    await setWriteState({
      state: "Write",
    })
    await setPageState({
      page: "Write",
    })
  }

  const onLoginSubmit = async (id, password, loginStat) => {
    await setPageState({
      page: "Main",
    })

    await setUserState({
      id: id,
      password: password,
      loginState: loginStat,
    })
  }

  const changePage = async(page) => {
    await setPageState({
      page: page,
    })
  }

  const changeCode = async(code) => {
    await setCodeState({
      code: code,
    })

    await setPredResult({
      pred_result: 0,
    })

    await setPageState({
      page: "Main",
    })
  }

  const get_pred_result = async () => {
    let filtered = []
    await axios.get("http://localhost:3001/pred_result")
      .then(res => {
        filtered = res.data.filter(data => data.code === codeState.code)
        console.log(filtered[0].pred)
        setPredResult({
          pred_result: filtered[0].pred,
        })
      })
  }

  const updateBoard = async (page) => {
    await setWriteState({
      state: "Update",
    })
    await setPageState({
      page: page,
    })
  }

  return (
    <div className="mapWrapper">
      <div className="App-Header">
        <Header id={sessionStorage.getItem("id")} loginStat={sessionStorage.getItem("loginStat")} onSubmit={onHeaderSubmit} />
      </div>
      <div className="App-Body">
        {pageState.page === "Main" && <Main code={codeState.code} />}
        {pageState.page === "Request" && <Request onSubmit={onRequestBoardSubmit} goWriteBoard={goWriteBoardSubmit} />}
        {pageState.page === "Change" && <Change code={codeState.code} onSubmit={changeCode} />}
        {pageState.page === "DetailBoard" && <Detail board={boardState.board} onSubmit={changePage} goUpdate={updateBoard} />}
        {pageState.page === "Register" && <Register onSubmit={changePage} />}
        {pageState.page === "Login" && <Login onSubmit={onLoginSubmit} />}
        {pageState.page === "Write" && <Writepage onSubmit={changePage} state={writeState.state} boardInfo={boardState.board} />}
        <Button onClick={get_pred_result} >클릭하여 예측결과 확인</Button> : {predResult.pred_result}
      </div>
    </div>
  );
}

export default App;
