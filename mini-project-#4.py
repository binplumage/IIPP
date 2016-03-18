"""
This module is implementation of classic arcade game Pong.
Player A (left) use the key "w"/"s" to control the paddle up/down.
Player B (right) use the key "up"/"down" to control the paddle up/down.
The ball  will continue speed up if the paddle hit the ball.
"""

import simplegui
import random
import math

# Initialize globals - pos and vel encode vertical info for paddles.
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2,  -2]
score1 = 0
score2 = 0
paddle1_pos = 200
paddle2_pos = 200

def spawn_ball(direction):
    """
    Initialize the postion and velocity for new ball in middle of table.
    The ball is toward to the previous winners direction.
    """
    global ball_pos, ball_vel # these are vectors stored as lists
    global score1, score2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120,240)/60
    ball_vel[1] = -(random.randrange(60,180)/60)
    if direction == LEFT :
        score1 = score1 + 1
        ball_vel[0] = - ball_vel[0]
    if direction == RIGHT:
        score2 = score2 + 1

def new_game():
    """
    Initialize parameter and start a new game.
    """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randrange(0,2))
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0


def draw(canvas):
    """
    Draw the game display.
    """
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1.5, "DeepPink", "HotPink")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel - HALF_PAD_HEIGHT >= 0 and paddle1_pos + paddle1_vel + HALF_PAD_HEIGHT <= HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel - HALF_PAD_HEIGHT >= 0 and paddle2_pos + paddle2_vel + HALF_PAD_HEIGHT <= HEIGHT:
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT),(0,paddle1_pos+HALF_PAD_HEIGHT)],1,"yellow","Orange")
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH,paddle2_pos-HALF_PAD_HEIGHT),(WIDTH,paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT)],1,"yellow","Orange")

    # determine whether paddle and ball collide
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ball_pos[1]>= paddle1_pos-HALF_PAD_HEIGHT-math.sqrt(BALL_RADIUS**2-(BALL_RADIUS-HALF_PAD_WIDTH)**2) and ball_pos[1] <= paddle1_pos+HALF_PAD_HEIGHT + math.sqrt(BALL_RADIUS**2-(BALL_RADIUS-HALF_PAD_WIDTH)**2):
            ball_vel[0] = -(ball_vel[0]*1.1)
            ball_vel[1] = ball_vel[1]*1.1
        else:
            spawn_ball(RIGHT)

    if ball_pos[0] >= WIDTH -(BALL_RADIUS+PAD_WIDTH):
        if ball_pos[1] >= paddle2_pos-HALF_PAD_HEIGHT-math.sqrt(BALL_RADIUS**2-(BALL_RADIUS-HALF_PAD_WIDTH)**2) and ball_pos[1] <= paddle2_pos+HALF_PAD_HEIGHT + math.sqrt(BALL_RADIUS**2-(BALL_RADIUS-HALF_PAD_WIDTH)**2):
            ball_vel[0] = -(ball_vel[0]*1.1)
            ball_vel[1] = ball_vel[1]*1.1
        else:
            spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(score1),[200,100],80,"Crimson")
    canvas.draw_text(str(score2),[380,100],80,"Crimson")

def keydown(key):
    """
    Deal with the event that key down.
    """
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5

def keyup(key):
    """
    Deal with the event that key up.
    """
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

def reset():
    global score1, score2
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset",reset)

# start frame
new_game()
frame.start()
