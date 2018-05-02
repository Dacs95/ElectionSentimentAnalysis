
var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');

var app = express();
var port = process.env.PORT || 8080;
var router = express.Router();
var MongoClient = require('mongodb').MongoClient;

var uri = "mongodb+srv://Dacs95:blanco12@cluster0-y8r2m.mongodb.net/sa-data";

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(__dirname + '/public'));
app.use('/static', express.static(__dirname + '/public'));

router.use(function(req, res, next){
    //do logging
    console.log('something is happening');
    next(); // make sure we go to the next routes and don`t stop here
});

router.get('/', function (req, res) {
    res.status(200).json({message:"Welcome from the coolest API!!!"});

});

router.get('/api/toptweets/:id',function(req,res){
    //llamar a mongo 
    MongoClient.connect(uri, function(err, client) {
        const collection = client.db("sa-data").collection("top-lopezobrador_");
        // perform actions on the collection object
        console.log(collection.find({}).next(function(err, doc){
            assert.equal(null, err);
            assert.ok(doc != null);
            client.close();
        }))
    });
    //Todo salio chido 
    res.status(200).json();
});

router.post('/api/session/', function (req, res) {
    console.log(req.body);
    res.status(200).json({'message' : 'posted'});
})

app.use('/', router);

app.listen(port);
console.log('server running on port ' + port);

