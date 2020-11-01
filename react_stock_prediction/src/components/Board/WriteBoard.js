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

  const writeBoard = () => {
      console.log("test")
  }

  return (
    <Card className={classes.root}>
        <CardContent className={classes.test}>
            <Typography className={classes.pos}>
                제목 : <input type="text" id="title" />
            </Typography>
            <Typography variant="body2" component="p">
                내용 : <input type="text" id="inner" />
                <br />
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small" onClick={writeBoard}>작성</Button>
        </CardActions>
    </Card>
  );
}

export default WriteBoard;