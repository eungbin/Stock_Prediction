import { Button } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import Card from './Card';
import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles({
    root: {
        width: "100%",
        height: "100%",
        display: "flex",
    },
});

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
            <div className={classes.root} >
                {changeList.list.map((data) => 
                    (
                    <Card key={data.code} code={data.code} />
                ))}
            </div>
        </>
    );
}

export default ChangeItem;
