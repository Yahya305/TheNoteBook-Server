const express = require("express");
const router = express.Router();
const jimp = require("jimp");
const multer = require("multer");
const fs = require("fs");
const Image = require("../models/Image");
// const blobUtil = require("blob-util");

const Storage = multer.memoryStorage();
const upload = multer({
  storage: Storage,
}).single("testImage");

router.post("/save", (req, res) => {
  try {
  upload(req, res, (err) => {
    if (err) {
      console.log(err);
      res.status(400).send({ message: "Some Error" });
    } else {
      const buffer = req.file.buffer;
      const newImage = new Image({
        name: req.body.name,
        image: {
          data: buffer,
          contentType: req.file.mimetype,
        },
      });
      newImage.save().then((_, rej) => {
        if (rej) {
          console.log(rej);
        } else {
          res.send({
            message: "successfully uploaded",
            imageData: newImage.image,
          });
        }
      });
      const fileName = "filename.jpg";
      fs.writeFile(fileName, buffer, "binary", (err) => {
        if (err) {
          console.log(err);
          return res.status(500).send({ message: "Server error" });
        }
      });
    }
  });
} catch (error) {
    res.status(500).send({message:"Internal Server Error"});
}
});

router.post("/edit", (req, res) => {
try {
  console.log("Request Received")
  upload(req, res, (err) => {
    if (err) {
      console.log(err);
    } else {
      jimp.read(req.file.buffer).then((image) => {
        for (let key in req.query) {
          image[key](
            req.query[key] !== "undefined"
              ? parseFloat(req.query[key])
              : undefined
          );
        }
        image
          .getBuffer(jimp.MIME_JPEG, (err, buffer) => {
            if (err) throw err;
            const newImage = new Image({
              name: req.body.name,
              image: {
                data: buffer,
                contentType: req.file.mimetype,
              },
            });
            res.send({ message: "successfully uploaded", imageData: buffer });
          })
          .write("../backend/modified.jpg");
      });
    }
  });
} catch (error) {
  res.status(500).send("Internal Server Error")
}
});
router.get("/find/:image_id", async (req, res) => {
    
  try {
    const image = await Image.findById(req.params.image_id);
    if (!image) {
      return res.status(404).send({ message: "Image not found" });
    }

    const fileData = image.image.data;
    console.log(image.image.contentType);
    console.log(fileData);
    // Save the image to local storage
    const fileName = "filenameee.jpg";
    fs.writeFile(fileName, fileData, "binary", (err) => {
      if (err) {
        console.log(err);
        return res.status(500).send({ message: "Server error" });
      }
      res.send({ message: "Image retrieved successfully", imageData: image });
    });
  } catch (err) {
    console.error(err);
    res.status(500).send({ message: "Internal Server Error" });
  }

});
router.delete("/delete/:image_id", async (req, res) => {
  try {
    const findImg = await Image.findById(req.params.image_id);
    if (!findImg) {
      res.status(404).send({ message: "Image Not Found" });
    }
    const deletedImage = await Image.findByIdAndDelete(req.params.image_id);
    res.status(200).send({ message: "Successfully Deleted" });
  } catch (error) {
    res.status(500).send({ message: "Internal Server Error" });
  }
});
module.exports = router;
