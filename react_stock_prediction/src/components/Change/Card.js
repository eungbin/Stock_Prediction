import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    flex: "none",
    align: "left",
    minWidth: 310,
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

export default function SimpleCard(props) {
  const classes = useStyles();

  const changeCode = () => {
    props.onSubmit(props.code)
  }

  return (
    <>
      <Paper className={classes.paper}>
        <h3>항목 변경 카드</h3>
        <h2>{props.code}.KS</h2>
        <br />
        <Button size="small" onClick={changeCode} >Change Item</Button>
      </Paper>
    </>
  );
}