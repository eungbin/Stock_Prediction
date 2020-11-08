const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = process.env.PORT || 3001;
const cors = require('cors');

app.use(cors());

var mysql = require('mysql');

var connection = mysql.createConnection({
    host: "localhost",
    port: 3306,
    user: "root",
    password: "vk2sjf12",
    database: "stock_prediction"
});

connection.connect()

app.use(bodyParser.json());

app.get('/pred_result', function (req, res) {
    connection.query("select * from pred_result", function (error, result, fields) {
        if(error) {
            res.send('err: ' + error);
        } else {
            console.log(result);
            res.send(result);
        }
    })
});

app.get('/data', function (req, res) {
    connection.query("select date, close from ?? order by date", req.query.code, function (error, result, fields) {
        if(error) {
            res.send("err: " + error);
        } else {
            res.send(result);
        }
    })
})

app.get('/request_board', function (req, res) {
    connection.query("select * from board order by no desc", function (error, result, fields) {
        if(error) {
            res.send("err: " + error);
        } else {
            res.send(result);
        }
    })
})

app.get('/changeList', function (req, res) {
    console.log("code : " + req.query.code);
    connection.query("select code from pred_result where code != ?", req.query.code, function (error, result, fields) {
        if(error) {
            res.send("err: " + error);
        } else {
            res.send(result);
        }
    })
})

app.post('/register', function (req, res) {
    let id = ""
    connection.query("select id from user where id=?", req.body.id, function (error, result, fields) {
        if(error) {
            res.send(error);
        } else {
            id = result
            if(id == "") {
                connection.query("insert into user(`id`, `password`) values(?, ?)", 
                [req.body.id, req.body.password], function (error, result, fields) {
                    if (error) {
                        console.log(error);
                        res.send(error);
                    } else {
                        console.log("회원가입 완료");
                        res.send(true);
                    }
                })
            } else {
                console.log("아이디 중복");
                res.send(false);
                return
            }
        }
    })
})

app.post('/login', function (req, res) {
    let id = "";
    connection.query("select id from user where id=? and password=?", 
    [req.body.id, req.body.password], function (error, result, fields) {
        if(error) {
            res.send(error);
        } else {
            console.log(result)
            id = result
            if(id == "") {
                console.log("아이디나 비밀번호 틀린듯");
                res.send(false);
                return
            } else {
                console.log("로그인 성공");
                res.send(true);
                return
            }
        }
    })
})

app.post('/writeboard', function(req, res) {
    connection.query("insert into board(`title`, `inner`, `writer`) values(?, ?, ?)", 
    [req.body.title, req.body.inner, req.body.id], function (error, result, fields) {
        if(error) {
            res.send(error);
        } else {
            console.log("글작성 완료");
            res.send(true);
        }
    })
})

app.post('/deleteboard', function(req, res) {
    console.log(req.body.board.board.no);

    connection.query("delete from board where no = ?", req.body.board.board.no, function (error, result) {
        if(error) {
            res.send(error);
        } else {
            console.log("삭제 완료");
            res.send(true);
        }
    })
})

app.post('/boardstate', function(req, res){
    connection.query("update board set status = ? where no = ?", [req.body.state, req.body.no], function (error, result) {
        if(error) {
            res.send(error);
        } else {
            console.log("변경 완료");
            res.send(true);
        }
    })
})



app.listen(port, ()=>{
    console.log(`express is running on ${port}`);
})