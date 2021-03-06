import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import './../../css/DetailBoard.css';
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

function DetailBoard(props) {
  const classes = useStyles();

  const [ boardState, setBoardState ] = useState({
    board: {},
  })

  useEffect(() =>  {
    setBoardState({
      board: props.board,
    })
  }, [props]);

  const deleteBoard = () => {
    axios.post("http://localhost:3001/deleteboard", {
        board: boardState
    }).then(res => {
        if(!(res.data)) {

        } else {
            alert("삭제 완료")
            props.onSubmit("Request")
        }
    })
  }

  const updateBoard = () => {
    props.goUpdate("Write", "Update")
  }

  const notCheck = () => {
    axios.post("http://localhost:3001/boardstate", {
        no: boardState.board.no,
        state: "미확인",
    }).then(res => {
        if(!(res.data)) {

        } else {
            alert("미확인으로 변경완료")
            props.onSubmit("Request")
        }
    })
  }

  const inProcessing = () => {
    axios.post("http://localhost:3001/boardstate", {
        no: boardState.board.no,
        state: "처리중",
    }).then(res => {
        if(!(res.data)) {

        } else {
            alert("처리중으로 변경완료")
            props.onSubmit("Request")
        }
    })
  }

  const processingComplete = () => {
    axios.post("http://localhost:3001/boardstate", {
        no: boardState.board.no,
        state: "처리완료",
    }).then(res => {
        if(!(res.data)) {

        } else {
            alert("처리완료로 변경완료")
            props.onSubmit("Request")
        }
    })
  }

  if(boardState.board.writer === sessionStorage.getItem("id") && sessionStorage.getItem("id") !== "admin") {
    return (
      <Card className={classes.root}>
          <CardContent className={classes.test}>
              <Typography className={classes.title} color="textSecondary" gutterBottom>
                  번호 : {boardState.board.no}
              </Typography>
              <Typography className={classes.pos}>
                  제목 : {boardState.board.title}
              </Typography>
              <Typography className={classes.pos}>
                  작성자 : {boardState.board.writer}
              </Typography>
              <Typography variant="body2" component="p">
                내용 : {boardState.board.inner}
                <br />
                <br />
              </Typography>
              <Typography variant="body2" component="p">
                {boardState.board.status}
                <br />
              </Typography>
          </CardContent>
          <CardActions>
            
              <Button size="small" onClick={updateBoard}>수정</Button>
              <Button size="small" onClick={deleteBoard}>삭제</Button>
          </CardActions>
      </Card>
    );
  } else if(sessionStorage.getItem("id") === "admin") {
    return (
      <Card className={classes.root}>
      <CardContent className={classes.test}>
          <Typography className={classes.title} color="textSecondary" gutterBottom>
              번호 : {boardState.board.no}
          </Typography>
          <Typography className={classes.pos}>
              제목 : {boardState.board.title}
          </Typography>
          <Typography className={classes.pos}>
              작성자 : {boardState.board.writer}
          </Typography>
          <Typography variant="body2" component="p">
            내용 : {boardState.board.inner}
            <br />
            <br />
          </Typography>
          <Typography variant="body2" component="p">
            {boardState.board.status}
            <br />
          </Typography>
      </CardContent>
      <CardActions>
          <Button size="small" onClick={updateBoard}>수정</Button>
          <Button size="small" onClick={deleteBoard}>삭제</Button>
          <Button size="small" onClick={notCheck}>미확인</Button>
          <Button size="small" onClick={inProcessing}>처리중</Button>
          <Button size="small" onClick={processingComplete}>처리완료</Button>
      </CardActions>
      </Card>
    )
  } else {
    return (
      <Card className={classes.root}>
        <CardContent className={classes.test}>
            <Typography className={classes.title} color="textSecondary" gutterBottom>
                번호 : {boardState.board.no}
            </Typography>
            <Typography className={classes.pos}>
                제목 : {boardState.board.title}
            </Typography>
            <Typography className={classes.pos}>
                작성자 : {boardState.board.writer}
            </Typography>
            <Typography variant="body2" component="p">
                내용 : {boardState.board.inner}
                <br />
                <br />
            </Typography>
            <Typography variant="body2" component="p">
                {boardState.board.status}
                <br />
            </Typography>
        </CardContent>
      </Card>
    );
  }
}

export default DetailBoard;