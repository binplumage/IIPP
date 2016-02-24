"""
This module is "Stopwatch: The Game".
"""
import simplegui

is_run = False
#If time arrived 10 mins, the game will stop.
is_end = False
counter = 0
x = 0
y = 0

def format(t):
    """
    This function is to convert in tenths of seconds into formatted string A:BC.D.
    """
    if t :
        A = t /600
        second = (t /10) % 60
        B = second / 10
        C = second % 10
        D = t % 10
        result = str(A)+":"+str(B)+str(C)+"."+str(D)
    else:
        result = "0:00.0"
    return result

def start():
    """
    Start the stopwatch for buttons "Start".
    """
    global is_run
    if not is_end:
        if not is_run:
            is_run = True
            timer.start()

def stop():
    """
    Stop the stopwatch for buttons "Stop".
    """
    global is_run, y, x
    if not is_end:
        if is_run :
            y = y + 1
            if (counter % 10) == 0:
                x = x + 1
        is_run = False
        timer.stop()

def reset():
    """
    Reset the stopwatch and record for buttons "Reset".
    """
    global counter, x, y, is_run
    counter = 0
    y = 0
    x = 0
    timer.stop()
    is_run = False


def timer_handler():
    """
    Define event handler for timer with 0.1 sec interval.
    """
    global counter, is_end
    if counter == 6000:
        is_end = True
    else:
        counter = counter + 1

def draw(canvas):
    """
    Draw the stopwatch and score.
    """
    canvas.draw_text(format(counter),[85,120],50,"white")
    canvas.draw_text(str(x)+"/"+str(y),[250,30],30,"Green")

# create frame
frame = simplegui.create_frame("Stopwatch",300,200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
timer = simplegui.create_timer(100,timer_handler)

# start frame
frame.start()
