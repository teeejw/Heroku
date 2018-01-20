var express = require('express');
var app = express();

var push = require('./routes/push');
var cascade = require('./routes/cascade');
var various = require('./routes/various');
var machinelearning = require('./routes/machinelearning');

app.set('port', (process.env.PORT || 5000));

app.use(express.static(__dirname + '/public'));

// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
  response.render('pages/index');
});

app.use('/push', push);
app.use('/cascade', cascade);
app.use('/various', various);
app.use('/machinelearning', machinelearning);

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});
