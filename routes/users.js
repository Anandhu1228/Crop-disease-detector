var express = require('express');
var router = express.Router();
const session = require('express-session');
const fs = require('fs');
const path = require('path');
const multer = require('multer');
const { spawn } = require('child_process');

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    const tempImageDir = path.join(__dirname, '../classifiers/temp_image');
    
    if (!fs.existsSync(tempImageDir)) {
      fs.mkdirSync(tempImageDir, { recursive: true });
    }

    cb(null, tempImageDir);
  },
  filename: function (req, file, cb) {
    cb(null, 'uploaded_image.jpg'); 
  }
});

const upload = multer({ storage: storage });

router.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: true,
}));

router.get('/', function(req, res, next) {
  res.render("user/front_page");
  return;
});

router.post('/get_plant', function(req, res, next) {
  req.session.plantId = req.body.plant;
  res.render("user/testpage");
});

router.post('/get_image', upload.single('image'), function(req, res, next) {
  try {
    const plant_id = req.session.plantId;
    const python = spawn('python', ['classifiers/classifier_file.py', plant_id], {
      stdio: ['pipe', 'pipe', 'pipe'],
    });

    let result = '';

    python.stdout.on('data', function (data) {
      result += data.toString();
    });

    python.stderr.on('data', function (data) {
      console.error(`stderr: ${data}`);
    });

    python.on('exit', function (code) {
      if (code === 0) {
        const lines = result.trim().split('\n');
        const prediction = lines[lines.length - 1];
        res.send({ prediction });
      } else {
        res.status(500).send('Error processing the image');
      }
    });

  } catch (err) {
    console.error("Error in processing image", err);
    res.status(500).send('Something went wrong');
  }
});

module.exports = router;
