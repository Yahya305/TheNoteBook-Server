const express = require("express");
const router = express.Router();
const { body, validationResult } = require("express-validator");
const Notes = require("../models/Notes");
const fetchuser = require("../middleware/fetchuser");
const { json } = require("express");

router.post(
  "/postnote",
  fetchuser,
  [
    body("title", "Enter a valid Title").isLength({ min: 1 }),
    // body("description", "Enter a valid Description").isLength({ min: 3 }),
    // body("author", "Enter a valid author").isLength({ min: 3 }),
    // body("tags", "Enter atleast one tag.").isLength({ min: 3 }),
    // body("date", "Invalid date.").isDate(),    //Not checking date bcz woh browser auto set krega
  ],
  async (req, res) => {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array()[0].msg });
      }
      const notes = new Notes({ ...req.body, user: req.user.id,author:req.user.firstName+" "+req.user.lastName });
      console.log(notes.id)
      await notes.save();
      //   console.log(req.body);
      const savedNote = await Notes.findById(notes.id);
      console.log(notes.user);
      // res.status(200).json({...req.body,_id:notes.id});
      res.status(200).json(savedNote);
    } catch (error) {
      console.log(error);
    }
  }
);
router.get("/fetchnotes", fetchuser, async (req, res) => {
  try {
    // const notes = await Notes.findById(req.user.id)
    console.log(req.user._id,">>>>")
    const notes = await Notes.find({ user: req.user.id });
    console.log("<<<<<")
    if (notes===null) {
      res.status(200).json({empty:"empty"});
      
    }
    console.log(notes);
    res.status(200).json(notes);
  } catch (error) {
    console.log("Internal Server Erroraaaa: ",error);
    // res.status(500).json({ message: "Internal Server Error" });
  }
});
router.put("/updatenote/:note_id", fetchuser, async (req, res) => {
  try {
    let note = await Notes.findById(req.params.note_id);
    if (!note) {
        res.status(404).json({ message: "Not Found" });
    }
    const note_uid = note.user;
    console.log("here________________________",req.user.id)
    if (!req.user.id) {
        res.status(401).json({ message: "Unauthorized Token" });
    }
    if (req.user.id != note_uid.toString()) {
        res.status(401).json({ message: "Unauthorized Token" });
    }
    const newNote = {};
    const { title, description, author, tags } = req.body;
    if (title) {
      newNote.title = title;
    }
    if (description) {
      newNote.description = description;
    }
    if (author) {
      newNote.author = author;
    }
    if (tags) {
      newNote.tags = tags;
      // console.log(tags,"oooooooooooooooooooooooooooooooooooooooooo")
    }
    note = await Notes.findByIdAndUpdate(
      req.params.note_id,
      { $set: newNote },
      { new: true }
    );
    // note.save();
    // res.status(200).json({ note });
    res.status(200).send(note);
  } catch (error) {
    console.log(error);
  }
});
router.delete("/deletenote/:note_id", fetchuser, async (req, res) => {
  try {
    const deleteNote = await Notes.findById(req.params.note_id);
    if (!deleteNote) {
      res.status(404).json({ error: "Note Not Found." });
    }
    if (deleteNote.user.toString() != req.user.id) {
      res.status(401).json({ error: "Invalid Token." });
    }
    const deletedNote = await Notes.findByIdAndDelete(req.params.note_id);
    res.status(200).json({ deletedNote });
  } catch (error) {
    console.log(error)
	// res.status(500).json({ message: "Internal Server Error" });
  }
});
router.get("/searchnotes/:key_word", async (req, res) => {
  try {
    const findNote = await Notes.find({
      $or: [{ title: { $regex: new RegExp(req.params.key_word, "i") } }],
    }).select("-user").select("-__v");
    if (findNote.length===0) {
      return res.status(201).json("No Suggestions." );
    }
    // res.status(200).json({ findNote });
    res.status(200).json(findNote);
  } catch (error) {
    console.log(error)
	res.status(500).json({ message: "Internal Server Error" });
  }
});
module.exports = router;