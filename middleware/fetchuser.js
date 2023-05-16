const jwt = require("jsonwebtoken");
require("dotenv").config({ path: ".env.local" });
const User = require("../models/User");

const fetchuser = async (req,res,next)=>{
    const token = req.header('auth-token');
    if (!token) {
        res.status(401).send({error:"Auth Token Missing"})
    }
    try {
        const data =  jwt.verify(token,process.env.TOKEN_SECRET);
        console.log(data,"kkkkkkkkkkkkkkkkk")
        // const user = await User.findById(data).select("-password");
        const user = await User.findById(data).select("-password")
        console.log(user,"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
        req.user=user;
        next();
    } catch (error) {
        console.log(token,"<<<<<<<<<<")
        res.status(401).send({error:"Please use the correct auth token"})
    }

}
module.exports = fetchuser;