// ref: https://expressjs.com/en/guide/routing.html
// ref: https://stackoverflow.com/questions/19696240/proper-way-to-return-json-using-node-or-express

const express = require('express')
const router = express.Router()

// middleware that is specific to this router
router.use((req, res, next) => {
  console.log('Time: ', Date.now())
  next()
})

router.get('/foo', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ response: "Hello" }));
})

router.get('/bar', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ response: "World" }));
})

module.exports = router
