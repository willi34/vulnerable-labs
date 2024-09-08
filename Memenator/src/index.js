const express = require('express');
const nunjucks = require('nunjucks');

const app = express();
const PORT = 3000;

nunjucks.configure('templates', {
  autoescape: false,
  express: app
});

app.use(express.urlencoded({ extended: true })); 
app.use(express.static('static'))

function makeTemplate(top, bottom, image) {
    var temp = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Page</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
            margin: 0;
            text-align: center;
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        .container {
            max-width: 600px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>` + top + `</h1>

        <img src="/images/` + image + `.jpg">
        
        <h1>` + bottom + `</h1>
    </div>
</body>
</html>
`
   var meme = nunjucks.renderString(
       str = temp
   );
   return meme;
}

function random() {
    const rand = Math.floor(Math.random() * (5 - 1 + 1)) + 1;
    return rand;
}

app.get('/', function(req, res) {
   return res.render('index.html')
});

app.post('/generate', function(req, res) {
   var top = req.body.top_text;
   var bottom = req.body.bottom_text;
   var img = random();
   var meme = makeTemplate(top, bottom, img);
   return res.send(meme);
});

app.listen(PORT);
