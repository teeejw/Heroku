var express = require('express');
var router = express.Router();


router.get('/', function(request, response) {
    response.render('./pages/cascade');
});

module.exports = router;
