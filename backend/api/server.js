
var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var cors = require('cors');

var app = express();
var port = process.env.PORT || 8080;
var router = express.Router();
var MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
var uri = "mongodb+srv://Dacs95:blanco12@cluster0-y8r2m.mongodb.net/sa-data";

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(__dirname + '/public'));
app.use('/static', express.static(__dirname + '/public'));
app.use(cors());
app.options('*', cors())

router.use(function(req, res, next){
    //do logging
    console.log('something is happening');
    next(); // make sure we go to the next routes and don`t stop here
});

router.get('/', function (req, res) {

    res.status(200).json({message:"Welcome from the coolest API!!!"});
});

router.get('/api/toptweets/:id', function(req,res){
    //llamar a mongo 
    console.log(req.params.id);
    name = req.params.id;
    collectionName = "top-" + name;
    var tweets =[];
    MongoClient.connect(uri, function(err, client) {
        const collection = client.db("sa-data").collection(collectionName);
        // perform actions on the collection object
        collection.find({}).toArray(function(err, docs){
            assert.equal(null, err);
            assert.ok(docs != null);

            console.log("Responding with top tweets of " + collectionName);
            client.close();

            res.status(200).json(docs);
        });
    });
});

router.get('/api/analysis/:id', function(req, res) {

});

router.get('/api/analysis/:id', function(req, res) {

});

router.post('/api/session/', function (req, res) {
    console.log(req.body);
    res.status(200).json({'message' : 'posted'});
})

app.use('/', router);

app.listen(port);
console.log('server running on port ' + port);

