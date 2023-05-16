const express = require("express");
const User = require("../models/User");
const router = express.Router();
const { body, validationResult } = require("express-validator");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
// require("dotenv").config({ path: ".env.local" }); //Use when run from backend folder
require("dotenv").config({ path: "./Backend/.env.local" }); //Use when npm run both
const fetchuser=require("../middleware/fetchuser");

router.post(
  "/Sign-in",
  [
    body("firstName", "Enter a valid name").isLength({ min: 3 }),
    body("lastName", "Enter a valid Last name").isLength({ min: 3 }),
    body("email", "Enter a valid email").isEmail(),
    // body('password','Enter a valid pasword').isLength({min:5})
    body("password", "Enter a valid pasword").isStrongPassword(),
  ],
  async (req, res) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array()[0].msg });
      }
      const salt = bcrypt.genSaltSync(10);
    //   const hash = bcrypt.hashSync("B4c0//", salt);
      const hash = bcrypt.hashSync(req.body.password, salt);
      req.body = { ...req.body, password: hash };
      const users = new User(req.body);
      console.log(process.env.TOKEN_SECRET);
      const secret = process.env.TOKEN_SECRET;
      const token = jwt.sign(users.id, secret);
      // can also be done using user.create
      // user = await User.create({
      //     firstName:req.body.firstName,
      //     lastName:....
      // })
      // lkn isme lambi ho jaige
      await users.save();
      console.log(req.body);
      res.status(200).json({...req.body, token});
    } catch (error) {
      console.log(error);
      if (error.message.includes("E11000")) {
        res.status(404).json({ error: "This email is already taken" });
      } else {
        res.status(404).json({ message: error.message });
      }
    }
  }
);

router.post(
  "/login",
  [
    body("email", "Enter a valid email").isEmail(),
    body("password", "Enter a valid pasword").isStrongPassword(),
  ],
  async (req, res) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ error: errors.array()[0].msg });
      }
      const { email, password } = req.body;
      const user = await User.findOne({ email });
      if (!user) {
        return res
          .status(400)
          .json({ error: "Please Enter Correct Credentials" });
      }
      const checkPassword = await bcrypt.compare(password, user.password);
      if (!checkPassword) {
        return res
          .status(400)
          .json({ error: "Please Enter Correct Credentials" });
      }
      const secret = process.env.TOKEN_SECRET;
      const token = jwt.sign(user.id, secret);
      // res.status(200).json([req.body, token]);
      res.status(200).json({...req.body, token,firstName:user.firstName,lastName:user.lastName});
    } catch (error) {
      console.log("Internal Server Error",error);
    }
  }
);

router.post("/getuser",fetchuser,(req,res)=>{
  try {
    // req.user is retrived using middleware (fetchuser)
    res.status(200).send(req.user)
  } catch (error) {
    console.log(error)
    res.send(error)
  }
})

module.exports = router;