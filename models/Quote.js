const mongoose = require('mongoose');
const { Schema } = mongoose;


const quotesSchema = new Schema({
  quote:{
    type: String,
    required: true
  },
  author:{
    type: String,
    required: true
  }
});


module.exports = mongoose.model('quote', quotesSchema,"quotes");