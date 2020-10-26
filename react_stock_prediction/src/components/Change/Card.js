import React from 'react';
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
    minWidth: 310,
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

export default function SimpleCard(props) {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
        <CardContent>
            <Typography className={classes.title} color="textSecondary" gutterBottom>
                항목 변경 카드
            </Typography>
            <Typography className={classes.pos} variant="h5" component="h2">
                {props.code}.KS
            </Typography>
            <Typography variant="body2" component="p">
                {props.code}.KS(으)로 변경하기.
                <br />
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small">Change Item</Button>
        </CardActions>
    </Card>
  );
}