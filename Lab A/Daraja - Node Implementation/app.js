const express = require('express');
const body_parser = require('body-parser');
const app = express();
const request = require('request');
app.use(body_parser.json());

//routes
app.get('/', (req, res) =>{
    res.send('App Set up Complete');
});

//Get Access Token
app.get('/access_token', (req, res) => {
    let url = "";
    let auth = new Buffer().toString('base64');

    request({
        url: "",
        headers: {
            "Authorization": "Basic " + auth
        }
       },
        (error, response, body) => {
            if(err){
                console.log(error)
            }else{
                res.status(200).json(body);
            }
        }
    )
});

//listen
app.listen(5000, (err, live) =>{
    if(err){
        console.error(err);
    }

    console.log("Server running on port 5000");
});