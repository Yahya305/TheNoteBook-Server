const  connectMongo= require("../db")
const express = require('express')
const cors = require('cors')
const app = express()
require("dotenv").config({ path: "./.env.local" })
const port = process.env.PORT || 5000

// app.use(cors({
//   origin:'http://localhost:3000',
//   origin:'http://192.168.18.54:3000',
// }))
const BASE_URL=process.env.BASE_URL
// const allowedOrigins = ['http://localhost:3000', 'http://192.168.18.54:3000'];
const allowedOrigins = ['http://localhost:3000', 'http://192.168.18.54:3000'];
const corsOptions = {
  origin: function (origin, callback) {
    console.log(origin)
    // check if the origin is allowed
    if (!origin) {
      // if no origin provided, allow the request
      return callback(null, true);
    }
    if (allowedOrigins.indexOf(origin) === -1) {
      console.log("Not Allowed")
      // if the origin is not allowed, reject the request
      return callback(new Error('Not allowed by CORS'));
    }
    // if the origin is allowed, allow the request
    console.log("Origin is allowed")
    return callback(null, true);
  }
};
app.use(cors(corsOptions));
connectMongo(app,port);


app.use(express.json())
app.use('/api/randomquote',require('../routes/quote'));
app.use('/api/notes',require('../routes/notes'))
app.use('/api/auth',require('../routes/auth'))
app.use('/api/imagelab',require('../routes/imagelab'))


// app.listen(port, () => {
//   console.log(`Example app listening on port ${port}`)
// })
module.exports = app;