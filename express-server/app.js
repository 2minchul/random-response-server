const express = require('express')
const uuid4 = require('uuid4')
const app = express()

const host = '0.0.0.0'
const port = 8080

app.get('/', (req, res) => {
  res.json({ 'id': uuid4(), 'time': Math.floor(new Date() / 1000) })
})

app.listen(port, host, () => {
  console.log(`Example app listening at http://${host}:${port}`)
})