/* 305 Assignment in Dart Pad
 * Uses given code to work with, which doesn't work with null safety on...
 * Task was to update the ball each frame.
 */

//Gage Hilyard
import 'dart:html';
import 'dart:math';
import 'dart:async';

CanvasElement canvas;
CanvasRenderingContext2D ctx;

void main() {
  MyScreen().run();
}

//holds ball location, size, and velocity
class Ball {
  num x = 50; //start x
  num y = 50; //start y
  num r = 15; //ball size (radius)
  num vx = 0; //velocity
  num vy = 0; //velocity
  
  //updates ball with physics
  void move() {
    // 1 - apply velocity to position (vx -> x)
    x += vx;
    y += vy;
    // 2 - apply drag/friction to velocity
    vx *= .99;
    vy *= .99;
    // 3 - apply gravity to velocity
    vy += .25;
    vx += .25;
  }
}

class MyScreen {  
  num _lastTimeStamp = 0;
  static const num GAME_SPEED = 1000 / 77;
  
  Ball ball;

  MyScreen() {
    canvas = querySelector('#surface') as CanvasElement;
    ctx = canvas.getContext('2d') as CanvasRenderingContext2D;
    
    ctx.fillStyle = 'green';
    ctx.strokeStyle = 'white';

    //Starts Screen
    clear();
    init();
    drawBall(ball.x, ball.y);
    canvas.onClick.listen(drawMove);
  }
  
  void init() {
    ball = Ball();
    print("canvas width: ${canvas.width}");
  }

  void clear() {
    ctx.fillStyle = 'purple';
    ctx.fillRect(0, 0, 400, 400);

  }
  
  void drawBall(x, y) {

    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.r, 0, 3.14 * 2);
    ctx.fillStyle = 'yellow';
    ctx.fill();
    ctx.closePath();
  }

  void drawMove(MouseEvent event) {
    ball.x = event.offset.x;
    ball.y = event.offset.y;
    clear();
    drawBall(ball.x, ball.y);
  }
  
  void checkForCollisions() {
    if (ball.y + ball.r > 400) {
      ball.y = 400 - ball.r;
      ball.vy = -ball.vy.abs();
    }
    if (ball.x + ball.r > 400) {
      ball.x = 400 - ball.r;
      ball.vx = -ball.vx.abs();
    }
    if (ball.y < 0) {
      ball.y = ball.r;
      ball.vy = ball.vy.abs();
    }
    if (ball.x < 0) {
      ball.x = ball.r;
      ball.vx = ball.vx.abs();
    }
  }
  
  Future run() async {
    update(await window.animationFrame);
  }

  void update(num delta) {
    final num diff = delta - _lastTimeStamp;

    if (diff > GAME_SPEED) {
      _lastTimeStamp = delta;
      clear();
      ball.move();
      checkForCollisions();
      drawBall(ball.x, ball.y);
    }
    run();
  }
}

