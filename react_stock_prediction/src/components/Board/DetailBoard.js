import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  root: {
    flex: "none",
    align: "left",
    width: 300,
    alignContent: "left",
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
    alignContent: "left",
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

  const testState = () => {
    console.log(props.board)
    console.log(boardState.board)
  }

  return (
    <Card className={classes.root}>
        <CardContent>
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
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small" onClick={testState}>TEST</Button>
        </CardActions>
    </Card>
  );
}

export default DetailBoard;