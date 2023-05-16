const express = require("express");
const router = express.Router();
const Quote = require("../models/Quote");

router.get("/",async(req,res)=>{
    try {
        const randomQuote= await Quote.findOne().skip(Math.round(Math.random()*102));
        res.send({quote:randomQuote.quote,author:randomQuote.author});
        // Could have used await Quote.count() which returns total no. of docs in a collection

    } catch (error) {
        console.log(error);
        res.status(500).send({message:"Internal Server Error"});
    }
})
module.exports = router;
