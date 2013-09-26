card_image = '/Users/SunnyYan/Dropbox/Codings/Python Projects/BlackJack/cards.png'
card_back = '/Users/SunnyYan/Dropbox/Codings/Python Projects/BlackJack/card_back.png'

CARD_SIZE = [73,98]
CARD_BACK_SIZE = [71,96]
RECT_POS1 = (650,50)
RECT_POS2 = (650,125)
RECT_POS3 = (650,200)
RECT_POS4 = (650,275)
RECT_SIZE1 = (140,50)
LABEL_POS1 = (690,60)
LABEL_POS2 = (702,135)
LABEL_POS3 = (682,210)
LABEL_POS4 = (673,285)
RESULT_POS = (250,500)
CAPTION_POS = (205,400)
SCORE_POS = (340,550)
RECT_BUTTON_COLOR = (255,255,255)

import random
import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,600),0, 32)
pygame.display.set_caption('The Blacjack Game')
screen.fill([15,155,4])
background = pygame.image.load(card_back).convert()
card_pic = pygame.image.load(card_image).convert()
playersName = pygame.font.SysFont("arial",20)
buttonFont = pygame.font.SysFont("arial",30)
labelFont = pygame.font.SysFont("arial", 40)



# initialize some useful global variables
in_play = False
outcome =""
score = 0
restart_Flag = 1

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if(suit in SUITS) and (rank in RANKS):
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
        card_location = (0.5+CARD_SIZE[0] *(RANKS.index(self.rank) ), CARD_SIZE[1] * (SUITS.index(self.suit)),
                         CARD_SIZE[0], CARD_SIZE[1])
        canvas.blit(card_pic, (pos[0],pos[1]), card_location)
                         

class Hand:
    def __init__(self):
        #self.num = []
        self.numlist = []
        self.numberlist = []
        self.num2 = []

    def __str__(self):
        self.add = "Hand.contains "
        for i in range (len(self.num)):
            self.add += self.num[i]
        return self.add
    
    def add_card(self,card):
        self.num2.append(card)
        self.numlist.append(card.rank)
        return self.num2

    def get_value(self):
        number = list(self.numlist)
        self.numberlist = list(self.numlist)
        k = 0
        outcome = 0
        for ch in number:
            self.numberlist[k] = VALUES[ch]
            if self.numberlist[k] != 1:
                outcome = outcome + self.numberlist[k]
            elif (self.numberlist[k] == 1) and ((outcome+10) < 21):
                outcome = outcome + self.numberlist[k] + 10
            else:
                outcome = outcome + self.numberlist[k]
            k = k + 1
        return outcome

    def draw(self, canvas, pos):
        for x in range(len(self.num2)):
            self.num2[x].draw(canvas, (pos[0] + x * (CARD_SIZE[0] + 20), pos[1]))
        

# define deck class
class Deck:
    def __init__(self):
        k = 0
        self.deck = range(len(SUITS) * len(RANKS))
        for suit in SUITS:
            for rank in RANKS:
                self.deck[k] = Card(suit, rank)
                k = k + 1
        

    def initialization(self):
        k = 0
        self.deck = range(len(SUITS) * len(RANKS))
        for suit in SUITS:
            for rank in RANKS:
                self.deck[k] = Card(suit, rank)
                k = k + 1
        return self.deck
        
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(len(self.deck) -1)

    def __str__(self):
        self.deckadd="Hand contains "
        for i in range(len(self.deck)):
            self.deckadd += str(self.deck[i]) + " "
        
def deal():
    global result, in_play, score, restart_Flag
    if (restart_Flag == 1):
        score = 0
        restart_Flag = 0
    result = "result comes here! "
    cards.shuffle()
    player.__init__()
    player.add_card(cards.deal_card())
    player.add_card(cards.deal_card())
    dealer.__init__()
    dealer.add_card(cards.deal_card())
    dealer.add_card(cards.deal_card())
    in_play = True


def hit():
    global in_play,score, result
    if in_play:
        player.add_card(cards.deal_card())
        if (player.get_value() >21):
            in_play = False
            score = score - 1
            result = " Result: Player lost! "

def stand():
    global in_play, score, result
    if in_play:
        while(dealer.get_value() < 17):
            dealer.add_card(cards.deal_card())
        if dealer.get_value() > 21:
            in_play = False
            score = score + 1
            result = " Result: Player Win!"
        elif dealer.get_value() > player.get_value():
            in_play = False
            score = score - 1
            result = " Result: Dealer Win! "
        else:
            in_play = False
            score = score + 1
            result = " Result: Player Win!"

def restart():
    global restart_Flag
    restart_Flag = 1
    deal()
    cards.__init__()
    
def text():
    screen.blit(buttonFont.render("Deal",0,(0,0,0)),LABEL_POS1)
    screen.blit(buttonFont.render("Hit",0, (0,0,0)),LABEL_POS2)
    screen.blit(buttonFont.render("Stand", 0, (0,0,0)), LABEL_POS3)
    screen.blit(buttonFont.render("Restart", 0, (0,0,0)), LABEL_POS4)
    screen.blit(labelFont.render(result, 0, (0,0,0)),RESULT_POS)
    screen.blit(playersName.render("Dealer",0,(0,0,0)),(50,20))
    screen.blit(playersName.render("Player",0,(0,0,0)),(50,220))
    screen.blit(labelFont.render("Welcome to Blackjack!", 0,(0,0,0)),CAPTION_POS)
    screen.blit(labelFont.render("Score: "+str(score), 0,(0,0,0)),SCORE_POS)

cards = Deck()
player = Hand()
dealer = Hand()
deal()

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            key_x,key_y = pygame.mouse.get_pos()
            
            print "key_x "+str(key_x)
            print "key_y "+str(key_y)
            if key_x >= 650 and ((key_y >= RECT_POS1[1]) and ( key_y<= RECT_POS1[1] +RECT_SIZE1[1])):
                deal()
            elif key_x >= 650 and ((key_y >=RECT_POS2[1]) and (key_y <= RECT_POS2[1] + RECT_SIZE1[1])):
                hit()
            elif key_x >= 650 and ((key_y >= RECT_POS3[1]) and (key_y <= RECT_POS3[1] + RECT_SIZE1[1])):
                stand()
            elif key_x >= 650 and ((key_y >= RECT_POS4[1]) and (key_y <= RECT_POS4[1] + RECT_SIZE1[1])):
                restart()
    screen.fill([15,155,4])
    screen.lock()
    pygame.draw.rect(screen, RECT_BUTTON_COLOR, Rect(RECT_POS1,RECT_SIZE1))
    pygame.draw.rect(screen, RECT_BUTTON_COLOR, Rect(RECT_POS2,RECT_SIZE1))
    pygame.draw.rect(screen, RECT_BUTTON_COLOR, Rect(RECT_POS3,RECT_SIZE1))
    pygame.draw.rect(screen, RECT_BUTTON_COLOR, Rect(RECT_POS4,RECT_SIZE1))
    screen.unlock()
    text()
    player.draw(screen, [50,250])
    
    dealer.draw(screen, [50,50])
    if in_play:
        screen.blit(background, (50,50))

    pygame.display.update()
