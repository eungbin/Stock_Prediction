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

function WriteBoard(props) {
  const classes = useStyles();

  useEffect(() =>  {
    setWriteState({
      state: props.state,
    })
  }, [props]);

  const [titleState, setTitleState] = useState({
    title: props.boardInfo.title,
  })

  const [innerState, setInnerState] = useState({
    inner: props.boardInfo.inner,
  })

  const [writeState, setWriteState] = useState({
    state: props.state,
  })

  const titleUpdate = (e) => {
    setTitleState({
        title: e.target.value,
    })
  }

  const innerUpdate = (e) => {
      setInnerState({
          inner: e.target.value,
      })
  }

  const write = () => {
    if(writeState.state === "Write") {
      console.log("write")
      axios.post("http://localhost:3001/writeboard", {
          title: titleState.title,
          inner: innerState.inner,
          id: sessionStorage.getItem("id"),
      }).then(res => {
          if(res.data) {
            alert("글작성 완료")
            props.onSubmit("Request")
          } else {
            console.log(res)
          }
      })
    } else if(writeState.state === "Update") {
      console.log("update")
      axios.post("http://localhost:3001/modifyboard", {
        no: props.boardInfo.no,
        title: titleState.title,
        inner: innerState.inner,
      }).then(res => {
        if(res.data) {
          alert("수정 완료")
          props.onSubmit("Request")
        } else {
          console.log(res)
        }
      })
    }
  }
  
  return (
    <Card className={classes.root}>
        <CardContent className={classes.test}>
            <Typography className={classes.pos}>
                제목 : <input type="text" id="title" value={titleState.title} onChange={(e) => titleUpdate(e)} />
            </Typography>
            <Typography variant="body2" component="p">
                내용 : <textarea rows="5" cols="20" id="inner" value={innerState.inner} onChange={(e) => innerUpdate(e)} />
                <br />
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small" onClick={write}>작성</Button>
        </CardActions>
    </Card>
  );
}

export default WriteBoard;