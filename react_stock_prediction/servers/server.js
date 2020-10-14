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
            console.log(result)
            res.send(result)
        }
    })
});

app.get('/data', function (req, res) {
    connection.query("select high from `005930` order by date", function (error, result, fields) {
        if(error) {
            res.send("err: " + error);
        } else {
            res.send(result)
        }
    })
})



app.listen(port, ()=>{
    console.log(`express is running on ${port}`);
})