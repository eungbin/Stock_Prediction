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

function App() {
  const [testState, setTestState] = useState({
    close: [],
    date: [],
  })

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

  useEffect(() =>  {
    console.log(codeState.code)
    axios.get("http://localhost:3001/data", {
        params: {
          code: codeState.code,
        }
      })
      .then(res => {
        let arr_date = []
        let arr_close = []
        console.log(res.data)
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

    await setPageState({
      page: "Main",
    })
  }

  const test_state = () => {
    console.log(pageState.page)
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
        <Header id={sessionStorage.getItem("id")} loginStat={sessionStorage.getItem("loginStat")} onSubmit={onHeaderSubmit} />
      </div>
      <div className="App-Body">
        {/* {pageState.page === "Main" && <Main date={testState.date} close={testState.close} />} */}
        {pageState.page === "Main" && <Main code={codeState.code} />}
        {pageState.page === "Request" && <Request onSubmit={onRequestBoardSubmit} goWriteBoard={goWriteBoardSubmit} />}
        {pageState.page === "Change" && <Change code={codeState.code} onSubmit={changeCode} />}
        {pageState.page === "DetailBoard" && <Detail board={boardState.board} onSubmit={changePage} />}
        {pageState.page === "Register" && <Register onSubmit={changePage} />}
        {pageState.page === "Login" && <Login onSubmit={onLoginSubmit} />}
        {pageState.page === "Write" && <Writepage onSubmit={changePage} boardInfo={boardState.board} />}
        {/* <button onClick={test_state}>Test</button> */}
      </div>
    </div>
  );
}

export default App;
