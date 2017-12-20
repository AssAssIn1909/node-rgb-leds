'use strict';

var app = require('express')(),
    http = require('http').Server(app),
    io = require('socket.io')(http),
    bodyParser = require('body-parser'),
    PythonShell = require('python-shell');

let block = false;
let currentColor = [0,0,0];
let speed = 8;

app.get('/', function(req, res){
    res.sendFile('/home/pi/node/index.html');
});

app.get('/jscolor.js', function(req, res){
    res.sendFile('/home/pi/node/jscolor.js');
})

io.on('connection', function(socket){
    socket.on('change', function(color){
        if(!block){
            var pyshell = new PythonShell('/home/pi/node/leds.py');
            block = true;
            var newColor = currentColor;
            newColor.push(color[0], color[1], color[2])
            var options = {
                uid: 0,
                mode: 'text',
                args: newColor
            };

            currentColor = color;
            console.log(newColor)
            pyshell.send(JSON.stringify(newColor));
            pyshell.on('message', function (message) {
                // received a message sent from the Python script (a simple "print" statement)
                console.log(message);
                block =false;
            });
            
            pyshell.end(function (err) {
                if (err){
                    throw err;
                };
            
                console.log('finished');
            });
        }
    });
});

http.listen(3000, function(){
    console.log('listening on *:3000');
});
