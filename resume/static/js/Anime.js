window.requestAnimFrame = (function() {
  return window.requestAnimationFrame     ||
    window.webkitRequestAnimationFrame    ||
    window.mozRequestAnimationFrame       ||
    window.oRequestAnimationFrame         ||
    window.msRequestAnimationFrame        ||
    function( callback ){
    window.setTimeout(callback, 1000/60);
  };
})();


var canvas = document.getElementById('animation');
var ctx = canvas.getContext('2d');
var W = window.innerWidth, H = window.innerHeight, linesListRight = [], linesListLeft = [];
var v = 1, mp = [0.03,-0.03, -0.05, 0.05, -0.07, 0.07], linesNum = 50, alphaParam = 10;
canvas.width = W;
canvas.height = H*2/5;

function paintOnCanvas(){

  ctx.clearRect(0, 0, W, canvas.height);
}

function LinesRight(){
  this.x = (1 - 2*Math.random())*W*5/4;
  this.y = -20*Math.random();
  this.xTo = this.x + Math.random()*300;
  this.yTo = canvas.height* Math.random();
  this.vxTo = v*mp[Math.floor(Math.random()*mp.length)];
  this.vyTo = v*mp[Math.floor(Math.random()*mp.length)];

  this.draw = function(){
    for (var j = 0; j < alphaParam; j++) {
      if (this.xTo > this.x + 31*j && this.xTo <  this.x + 31*(j+1) || this.xTo < this.x - 31*j && this.xTo > this.x -31*(j+1)) {
        ctx.globalAlpha = 1 - 0.1*j;
      }
    }

    ctx.strokeStyle = "#FFF";
    ctx.beginPath();
    ctx.lineWidth = 0.3;
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(this.xTo, this.yTo);
    ctx.stroke();
  }
}

function LinesLeft(){
  this.x = (1 - 2*Math.random())*5/4*W;
  this.y = -20*Math.random();
  this.xTo = this.x - Math.random()*300;
  this.yTo = canvas.height* Math.random();
  this.vxTo = v*mp[Math.floor(Math.random()*mp.length)];
  this.vyTo = v*mp[Math.floor(Math.random()*mp.length)];

  this.draw = function(){
    for (var j = 0; j < alphaParam; j++) {
      if (this.xTo > this.x + 31*j && this.xTo <  this.x + 31*(j+1) || this.xTo < this.x - 31*j && this.xTo > this.x -31*(j+1)) {
        ctx.globalAlpha = 1 - 0.1*j;
      }
    }

    ctx.strokeStyle = "#FFF";
    ctx.beginPath();
    ctx.lineWidth = 0.3;
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(this.xTo, this.yTo);
    ctx.stroke();
  }
}

for (var i = 0; i < linesNum; i++) {
  linesListRight.push(new LinesRight());
  linesListLeft.push(new LinesLeft());
}


function fillBoard(){
  paintOnCanvas();

  for (var i = 0; i < linesListRight.length; i++) {
    lineR = linesListRight[i];
    lineL = linesListLeft[i];
    lineR.draw();
    lineL.draw();
  }

  update();

}

function update(){

  for (var i = 0; i < linesListRight.length; i++) {
    lineR = linesListRight[i];
    lineL = linesListLeft[i];

    lineR.xTo += lineR.vxTo;
    lineR.yTo += lineR.vyTo;

    lineL.xTo += lineL.vxTo;
    lineL.yTo += lineL.vyTo;


  if (lineR.yTo > canvas.height || lineR.yTo < lineR.y + 20) {
    lineR.vyTo = -lineR.vyTo;

  }
  if (lineR.xTo > lineR.x + 300 || lineR.xTo < lineR.x - 300) {
    lineR.vxTo = -lineR.vxTo;
    lineR.vyTo = -lineR.vyTo;
  }

  if (lineL.yTo > canvas.height || lineL.yTo < lineL.y + 20) {
    lineL.vyTo = -lineL.vyTo;
  }

  if (lineL.xTo > lineL.x + 300 || lineL.xTo < lineL.x - 300) {
    lineL.vxTo = -lineL.vxTo;
    lineL.vyTo = -lineL.vyTo;
  }

}
}

function animloop() {
  requestAnimFrame(animloop);
  fillBoard();
  update();
}
animloop();
