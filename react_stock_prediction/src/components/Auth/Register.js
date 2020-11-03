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

function Register(props) {
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
    props.onSubmit("Main");
  }

  const register = () => {
    console.log(idState.id)
    console.log(passwordState.password)

    if(idState.id === "") {
        alert("아이디를 입력해 주세요.")
        return
    } else if(passwordState.password === "") {
      alert("비밀번호를 입력해 주세요.")
        return
    }

    axios.post("http://localhost:3001/register", {
        id: idState.id,
        password: passwordState.password,
    }).then(res => {
        if(!(res.data)) {
            alert("아이디 중복")
        } else {
            alert("회원가입 완료!")
            goMain()
        }
    })
  }

  return (
    <Card className={classes.root}>
        <CardContent className={classes.test}>
            <Typography className={classes.title}>
                회원가입<br />
            </Typography>
            <Typography className={classes.pos}>
                아이디 : <input type="text" name="id" placeholder="아이디" onChange={(e) => idUpdate(e)} />
            </Typography>
            <Typography className={classes.pos}>
                비밀번호 : <input type="password" name="password" placeholder="비밀번호" onChange={(e) => passwordUpdate(e)} />
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small" onClick={register}>REGISTER</Button>
        </CardActions>
    </Card>
  );
}

export default Register;