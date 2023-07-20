const path = require('path');
const express = require('express');
const { spawn } = require('child_process');
const bodyParser = require('body-parser');

const port = 3000;

const app = express();
const urlencodedParser = bodyParser.urlencoded({ extended: false })

app.route('/')
  .get((req, res) => {
    const root = path.join(__dirname, "views");
    const options = {
        "root" : root
    };
    res.sendFile('index.html', options, (err) => {
        if(err) {
            next(err);
        } else {
            console.log("File successfully rendered!");
        }
    })
  })
  .post(urlencodedParser, (req, res) => {
    if(req._body) {
        let modelArguments = [];
        modelArguments.push('model_trigger.py');
        let inputs = Object.values(req.body);
        inputs.forEach((inputs) => modelArguments.push(String(inputs)));

        let result = ""
        const modelTriggerChild = spawn('python', modelArguments);
        modelTriggerChild.stdout.on('data', (data) => {
          console.log(`stdout: ${data}`);
          result = data;
          res.send(`Attrition Probability: ${result}`);
        });
        modelTriggerChild.stderr.on('data', (data) => {
          console.error(`stderr: ${data}`);
        });
        modelTriggerChild.on('close', (code) => {
          console.log(`child process exited with code ${code}`);
        });   
    }
  })


app.listen(port, () => {
  console.log(`Server running on port: ${port}`)
})

