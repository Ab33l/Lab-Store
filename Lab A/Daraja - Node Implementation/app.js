const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const request = require('request');
const os = require('os');
app.use(bodyParser.json());


function getLocalTime() {
    const now = new Date();
    return now.toLocaleTimeString();
}

//routes
app.get('/', (req, res) =>{
    const localTime = getLocalTime();
    //req.send('App Set up Complete');
    res.send('Your local time is ' + localTime);

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
            "ShortCode": "ShortCode",
            "ResponseType":"Completed",
            "ConfirmationURL":"http://IP_Address:Port/confirmation",
            "ValidationURL":"http://IP_Address:Port/validation"
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



app.post('/confirmation', (req, res) =>{
    console.log('......confirmation-----');
    console.log(req.body)
})

app.post('/validation', (req, res) =>{
    console.log('......validation-----');
    console.log(req.body)
})


app.get('/simulate', access, (req,res) => {
    let url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate";
    let auth = 'Bearer ' + req.access_token

    request({
        url:url,
        method:"POST",
        headers:{
            'Authorization': auth 
        },
        json: {
            'ShortCode': 'ShortCode',
            'CommandID': 'CustomerPayBillOnline',
            'Amount': '100',
            'Msisdn': '254708374149',
            'BillRefNumber': 'PaybillOnlineHeretoo'
        }
    },
    function(err,response,body){
        if(err){
            console.log(err)
        }else{
            res.status(200).json(body)
        }
    }
    )
})

function access(req, res, next){
    let url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials';
    let auth = new Buffer('Consumer_Secret:Consumer_Key').toString('base64');

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

//get balance 
app.get('/balance', access, (res,req) =>{
    let endpoint = 'https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query';
    let auth = 'Bearer ' + req.access

    request({
        url:endpoint,
        method:'POST',
        headers: {
            'Authorization': auth
        },
        json:{
            "Initiator": "testapi",
            "SecurityCredential": "",
            "CommandID": "AccountBalance",
            "PartyA": '600984',
            "IdentifierType": '4',
            "Remarks": "Remarks",
            'QueueTimeoutURL': 'http://IP_Address:Port/AccountBalance/queue',
            'ResultURL': 'http://IP_Address:Port/AccountBalance/result'
        }
    }
    )
})

app.post('/AccountBalance/queue', (req, res) =>{
    console.log('......Balance Timeout Response-----');
    console.log(req.body)
})

app.post('/AccountBalance/result', (req, res) =>{
    console.log('......Balance Request Response-----');
    console.log(req.body)
})

//listen
app.listen(5000, (err, live) =>{
    if(err){
        console.error(err);
    }

    console.log("Server running on port 5000");
});