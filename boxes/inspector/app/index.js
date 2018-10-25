'use strict'

var express = require('express')
var bodyParser = require('body-parser')
var session = require('express-session')
var md5 = require('md5')
const { exec } = require('child_process')

var app = express()

app.use(bodyParser.urlencoded({
  extended: true
}))

app.use(session({
  secret: 'cookie_secret',
  name: 'login-cookie',
  resave: true,
  saveUninitialized: true
}))

app.use(express.static('public'))

app.set('view engine', 'pug')

app.get('/', function (req, res) {
  res.render('index', { title: '- Hello world!' })
})

app.get('/secure', function (req, res) {
  // Only load if the session value is set
  if (req.session.loggedIn === 'true') {
    if (typeof req.session.output !== 'undefined') {
      res.render('secure', { dataout: req.session.output })
    } else {
      res.render('secure')
    }
  } else {
    res.redirect('/')
  }
})
app.post('/secure', function (req, res) {
  // Only load if the session value is set
  if (typeof req.body.loginName !== 'undefined' && typeof req.body.loginPass !== 'undefined') {
    if (req.body.loginName === 'admin' && md5(req.body.loginPass) === '46f94c8de14fb36680850768ff1b7f2a') {
      req.session.loggedIn = 'true'
      res.render('secure')
    } else {
      req.session.loggedIn = 'false'
      res.render('error', { msg: 'Username or password incorrect', status: '400' })
    }
  } else {
    throw new Error('Need both a username and password')
  }
})

app.post('/ping', function (req, res) {
  if (req.session.loggedIn === 'true') {
    // let result = null
    let cmdstr = 'ping -c 3 ' + req.body.addrToPing

    exec(cmdstr, (err, stdout, stderr) => {
      if (err) {
        console.error(`exec error: ${err}`)
        return
      }
      stdout = stdout.replace(/(?:\r\n|\r|\n)/g, '<br>')
      req.session.output = stdout
      res.redirect('/secure')
    })
  } else {
    throw new Error('Not logged in!')
  }
})

// Catch 404
app.use(function (req, res, next) {
  var err = new Error('Not Found')
  err.status = 404
  next(err)
})

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message
  res.locals.error = req.app.get('env') === 'development' ? err : {}

  // render the error page
  res.status(err.status || 500)
  res.render('error', { msg: err.message, status: err.status })

  console.log(err)
})

app.listen(80, function () {
  console.log('Listening on port 80')
})
