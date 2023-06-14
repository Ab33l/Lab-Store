const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const request = require('request');
app.use(bodyParser.json());

//routes
app.get('/', (req, res) =>{
    res.send('App Set up Complete');
});

//Get Access Token
app.get('/access_token', access, (req, res) => {
    res.status(200).json({access_token: req.access_token})
});

//Register URLs
app.get('/register', access, (req,res) => {
    let url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl";
    let auth = "Bearer " + req.access_token

    request({
        url:url,
        method:"POST",
        headers:{
            "Authorization": auth
        },
        json: {
            "ShortCode": "601426",
            "ResponseType":"Completed",
            "ConfirmationURL":"ConfirmationURL",
            "ValidationURL":"ValidaitonURL"
        }
    },
    function(err,body,response){
        if(err){
            console.log(err);
        }
        res.status(200).json(body)
    }
    )
})

function access(req, res, next){
    let url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials';
    let auth = new Buffer('ConsumerKey:ConsumerSecret').toString('base64');

    request({
        url: url,
        headers: {
            'Authorization': 'Basic ' + auth
        }
       },
        (err, response, body) => {
            if(err){
                console.log(error);
            }else{
                req.access_token = JSON.parse(body).access_token
                next()
            }
        }
    )
}

//listen
app.listen(5000, (err, live) =>{
    if(err){
        console.error(err);
    }

    console.log("Server running on port 5000");
});