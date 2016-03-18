"""
This module is implementation of card game - Memory.
Memory is a card game in which the player deals out a set of cards face down.
In Memory, a turn consists of the player flipping over two cards.
If they match, the player leaves them face up.
If they don't match, the player flips the cards back face down.
The goal of Memory is to end up with all of the cards flipped face up in the minimum number of turns. 
"""

import simplegui
import random

# helper function to initialize globals
def new_game():
    """
    Start a new game and initialize all global variables.
    """
    global cards, state, exposed, turn, exposed_card
    exposed_card = [0, 0]
    cards = range(8)
    cards = cards + range(8)
    random.shuffle(cards)
    state = 0
    turn = 0
    label.set_text("Turns = 0")
    exposed = range(16)
    for index in range(16):
        exposed[index] = False

def mouseclick(pos):
    """
    Determine if two exposed card are the same.
    """
    global exposed, state, turn, exposed_card

    click_pos = pos[0]//50
    if not exposed[click_pos] :
        exposed[click_pos] = True
        if state == 0:
            turn = turn + 1
            exposed_card[0] = click_pos
            state = 1
        elif state == 1:
            exposed_card[1] = click_pos
            state = 2
        else:
            turn = turn + 1
            if cards[exposed_card[0]] != cards[exposed_card[1]]:
                exposed[exposed_card[0]] = False
                exposed[exposed_card[1]] = False
            exposed_card[0] = click_pos
            state = 1
        text = "Turns = "+ str(turn)
        label.set_text(str(text))

def draw(canvas):
    """
    Draw the game display.
    """
    global exposed
    canvas.draw_polygon([(0, 0), (0, 100), (800, 100), (800, 0)], 1, 'balck', 'green')
    card_pos = [0 , 65]
    for card_index in range(len(cards)):
        card_pos[0] = card_index * 50 +10
        line_pos = card_index * 50
        canvas.draw_line([line_pos, 0], [line_pos, 100], 1, 'black')
        if exposed[card_index]:
            canvas.draw_polygon([(card_index*50, 0), (card_index*50, 100), ((card_index*50)+50, 100), ((card_index*50)+50, 0)], 1, 'black', 'white')
            canvas.draw_text(str(cards[card_index]), card_pos, 50, '#FF69B4')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
