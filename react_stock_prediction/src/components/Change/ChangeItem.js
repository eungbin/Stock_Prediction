import { Button } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import Cards from './Card';
import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
      },
}));

function ChangeItem(props) {
    const classes = useStyles();

    const [ changeList, setChangeList ] = useState({
        list: [],
    })

    const [ codeState, setCodeState ] = useState({
        code: props.code,
    })

    useEffect(() =>  {
        axios.get("http://localhost:3001/changeList", {
                params: {
                    code: codeState.code,
                }
            })
          .then(res => {
            let list_changeList = []
            res.data.map(data => {
              list_changeList.push(data)
            })
            setChangeList({
                list: list_changeList,
            })
          })
      }, []);


    return (
        <>
            <div className={classes.root}>
                <Grid container spacing={3}>
                    {changeList.list.map((data) => 
                        (
                            <Grid item xs={3} key={data.code}>
                                <Cards key={data.code} code={data.code} onSubmit={props.onSubmit}/>
                            </Grid>
                    ))}
                </Grid>
            </div>
        </>
    );
}

export default ChangeItem;
