"""
This module is Blackjack.
An ace may be valued as either 1 or 11,
face cards are valued at 10 and the value of the remaining cards corresponds to their number.
The players plays against a dealer with the goal of building a hand
whose cards have a total value that is higher than the value of the dealer's hand, but not over 21.
The player is "busted" if the player's hand exceeds 21.
The player may "stand" and the dealer will then hit his hand until the value of his hand is 17 or more.
If the dealer busts, the player wins.
Otherwise, the player and dealer then compare the values of their hands and the hand with the higher value wins.
The dealer wins ties in this version.
"""

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    """
    Define a card class.
    """
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    """
    Define a hand card class.
    """
    def __init__(self):
        self.hand = []

    def __str__(self):
        ans = "Hand contains"
        for i in range(len(self.hand)):
            ans = ans + " " + str(self.hand[i])
        return ans

    def add_card(self, card):
        """
        Add a card object to a hand.
        """
        self.hand.append(card)

    def get_value(self):
        """
        Compute the value of the hand.
        Count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        """
        values = 0
        IS_A = False
        for card in self.hand:
            values += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                IS_A = True
        if IS_A:
            if values + 10 <= 21:
                values += 10
        return values

    def draw(self, canvas, pos):
        """
        Draw a hand on the canvas, use the draw method for cards
        """
        offset = 80
        for card in self.hand:
            pos[0] += offset
            card.draw( canvas, pos)

class Deck:
    """
    Define deck class.
    """
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for values in VALUES:
                card = Card(suit, values)
                self.deck.append(card)

    def shuffle(self):
        """
        Shuffle the deck
        """
        random.shuffle(self.deck)

    def deal_card(self):
        """
        Deal a card object from the deck
        """
        return self.deck.pop()

    def __str__(self):
        result = "Deck contains"
        for i in self.deck:
            result = result + " " + str(i)
        return result

def deal():
    """
    Restart a new turn.
    Deal a card to player and dealer.
    """
    global outcome, in_play, score, my_deck, player_hand, dealer_hand

    outcome = ""
    if in_play:
        score -= 1
    my_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    my_deck.shuffle()
    for i in range(0,2):
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
    in_play = True

def hit():
    global in_play, outcome, score
    """
    Hit the player.
    """
    if in_play:
        player_hand.add_card(my_deck.deal_card())
        if player_hand.get_value()>21:
            outcome = "You have busted."
            in_play = False
            score -= 1


def stand():
    global in_play, outcome, score
    """
    After player "stand", repeatedly hit dealer until his hand has value 17 or more.
    """
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        if player_hand.get_value() <= dealer_hand.get_value() and dealer_hand.get_value()<=21:
            outcome = "You lose."
            in_play = False
            score -= 1
        else:
            outcome = "You win."
            in_play = False
            score += 1

def draw(canvas):
    """
    Draw the game display.
    """
    score_text = 'score : ' + str(score)
    player_hand.draw(canvas, [20, 400])
    dealer_hand.draw(canvas, [20, 150])
    if  in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136, 198], CARD_BACK_SIZE)
    canvas.draw_text('Blackjack', (100, 90), 50, '#48D1CC')
    canvas.draw_text('Dealer', (100, 140), 30, '#191970')
    canvas.draw_text('Player', (100, 380), 30, '#191970')
    canvas.draw_text(outcome, (300, 140), 30, '#191970')
    canvas.draw_text(score_text, (400, 90), 40, '#191970')
    if in_play:
        canvas.draw_text('Hit or stand?', (300, 380), 30, '#191970')
    else:
        canvas.draw_text('New deal?', (300, 380), 30, '#191970')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
