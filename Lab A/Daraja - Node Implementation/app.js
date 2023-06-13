const express = require('express');
const body_parser = require('body-parser');
const app = express();
app.use(body_parser.json());

//routes
app.get('/', (req, res) =>{
    res.send('App Set up Complete');
});

//listen
app.listen(5000);