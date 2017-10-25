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
    res.sendFile('/home/osmc/rpi_ws281x/python/nodejs/index.html');
});

app.get('/jscolor.js', function(req, res){
    res.sendFile('/home/osmc/rpi_ws281x/python/nodejs/jscolor.js');
})

io.on('connection', function(socket){
    socket.on('change', function(color){
        if(!block){
            block = true;
            console.log(color);
            var newColor = currentColor;
            newColor.push(color[0], color[1], color[2])
            var options = {
                uid: 0,
                mode: 'text',
                args: newColor
            };
            console.log(newColor);

            currentColor = color;

            PythonShell.run('leds.py', options, function(err, result){
                if(err) throw err;
                else{
                    console.log(result);
                    block = false;
                };
            });            
        }
    });
});

http.listen(3000, function(){
    console.log('listening on *:3000');
});

function colorChange(index){
    console.log(index);
    if(currentColor[index] > setColor[index]){
        if(currentColor[index] - setColor[index] > speed)
            currentColor[index] -= speed;
        else
            currentColor[index] = setColor[index]
    }else if(currentColor[index] < setColor[index]){
        if(setColor[index] - currentColor[0] > speed)
            currentColor[index] += speed;
        else
            currentColor[index] = speed;
    }
}