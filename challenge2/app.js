
// load express module
const express = require('express')
var app = express()

// get port and base_url from env
// set default if it is empty
var port = (process.env.port || '3000')
var base_url = (process.env.base_url || 'conabio')

// include routes
const route = require('./routes.js')
app.use( '/'+base_url , route)

// start to listen
app.listen(port, () => {
  console.log(`base_url ${base_url}`)
  console.log(`Example app listening on port ${port}`)
})