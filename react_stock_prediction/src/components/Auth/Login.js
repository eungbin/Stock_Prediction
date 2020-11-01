import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import axios from 'axios';

const useStyles = makeStyles({
  root: {
    flex: "none",
    align: "left",
    width: "100%",
  },
  title: {
    fontSize: 16,
  },
  pos: {
    marginBottom: 12,
  },
});

function Login(props) {
  const classes = useStyles();
  
  const [ idState, setIdState ] = useState({
    id: "",
  })

  const [ passwordState, setPasswordState ] = useState({
    password: "",
  })

  const idUpdate = (e) => {
    setIdState({
        id: e.target.value,
    })
  }

  const passwordUpdate = (e) => {
      setPasswordState({
          password: e.target.value,
      })
  }

  const goMain = () => {
    sessionStorage.setItem("loginStat", true);
    sessionStorage.setItem("id", idState.id);
    sessionStorage.setItem("pw", passwordState.password);
    props.onSubmit(idState.id, passwordState.password, true);
    // window.location.reload(true);
  }

  const login = () => {
    console.log(idState.id)
    console.log(passwordState.password)

    if(idState.id === "") {
        console.log("아이디를 입력해 주세요.")
        return
    } else if(passwordState.password === "") {
        console.log("비밀번호를 입력해 주세요.")
        return
    }

    axios.post("http://localhost:3001/login", {
        id: idState.id,
        password: passwordState.password,
    }).then(res => {
        if(!(res.data)) {
            alert("아이디 혹은 비밀번호를 확인해주세요.")
        } else {
            alert("로그인 성공!")
            goMain()
        }
    })
  }

  return (
    <Card className={classes.root}>
        <CardContent className={classes.test}>
            <Typography className={classes.title}>
                로그인<br />
            </Typography>
            <Typography className={classes.pos}>
                아이디 : <input type="text" name="id" placeholder="아이디" onChange={(e) => idUpdate(e)} />
            </Typography>
            <Typography className={classes.pos}>
                비밀번호 : <input type="text" name="password" placeholder="비밀번호" onChange={(e) => passwordUpdate(e)} />
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small" onClick={login}>LOGIN</Button>
        </CardActions>
    </Card>
  );
}

export default Login;