import React, { useEffect, useState } from 'react';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableHead from '@material-ui/core/TableHead';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { Button } from '@material-ui/core';

const StyledTableCell = withStyles((theme) => ({
    head: {
        backgroundColor: theme.palette.common.white,
        color: theme.palette.common.black,
      },
      body: {
        fontSize: 14,
      },
  }))(TableCell);
  
  const StyledTableRow = withStyles((theme) => ({
    root: {
      '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover,
      },
    },
  }))(TableRow);

const useStyles = makeStyles({
    table: {
      minWidth: 700,
    },
});

export default function RequestBoard(props) {
    const classes = useStyles();
    const [ boardState, setBoardState ] = useState({
        data: [],
    });

    useEffect(() =>  {
        axios.get("http://localhost:3001/request_board")
          .then(res => {
            let list_board = []
            res.data.map(data => {
              list_board.push(data)
            })

            setBoardState({
                data: list_board,
            })
          })
    }, []);

    const showDetail = (no, title, inner, writer, status) => {
        const boardInfo = {
            no: no,
            title: title,
            inner: inner,
            writer: writer,
            status: status
        }
        props.onSubmit(boardInfo)
    }

    const writeBoard = () => {
      if(sessionStorage.loginStat === "true") {
        props.goWriteBoard()
      } else {
        alert("로그인 후 작성 가능합니다.")
      }
    }

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <StyledTableCell>번호</StyledTableCell>
                        <StyledTableCell>제목</StyledTableCell>
                        <StyledTableCell>작성자</StyledTableCell>
                        <StyledTableCell>상태</StyledTableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                {boardState.data.map((b) => (
                    <StyledTableRow key={b.no} onClick={e => showDetail(b.no, b.title, b.inner, b.writer, b.status)}>
                        <StyledTableCell component="th" scope="b">
                            {b.no}
                        </StyledTableCell>
                        <StyledTableCell>{b.title}</StyledTableCell>
                        <StyledTableCell>{b.writer}</StyledTableCell>
                        <StyledTableCell>{b.status}</StyledTableCell>
                    </StyledTableRow>
                ))}
                </TableBody>
            </Table>
            <Button onClick={writeBoard}>글 작성</Button>
        </TableContainer>
    );
}