var bodyParser = require('body-parser');
var cors = require('cors');
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var passport = require('passport');

var auth = require('./routes/auth');
var index = require('./routes/index');
var news = require('./routes/news');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, '../client/build/'));
app.set('view engine', 'jade');
app.use('/static', express.static(path.join(__dirname, '../client/build/static/')));

app.use(bodyParser.json());
//TODO: remove this after development is done
app.use(cors());


var config = require('./config/config.json');
require('./models/main.js').connect(config.mongoDbUri);

app.use(passport.initialize());
var localSignupStrategy = require('./passport/signup_passport');
var localLoginStrategy = require('./passport/login_passport');
passport.use('local-signup', localSignupStrategy);
passport.use('local-login', localLoginStrategy);

const authCheckMiddleWare = require('./middleware/auth_checker');
app.use('/news', authCheckMiddleWare);

app.use('/', index);
app.use('/auth', auth);
app.use('/news', news);

// catch 404 and forward to error handler
app.use(function(req, res) {
  var err = createError(404)
  res.render('404 Not Found');
});


module.exports = app;
