# Implement of card game - Memory

import random
import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((900,100), 0, 32)
pygame.display.set_caption('Card Game-----------Memory')

screen.fill([0,0,0])
font = pygame.font.Font(None, 80)
font2 = pygame.font.Font(None,30)
font3 = pygame.font.SysFont("arial", 28)

def init():
    global x, card, state, steps, image,text
    steps = 0
    card = range(17)
    state = 0
    x = range(8)
    y=range(8)
    x.extend(y)
    random.shuffle(x)
    text = []
    
def mouseclick(pos):
    global x, num_cards, state, card, num1,num2,num_cards1,num_cards2,steps
    if pos[0]<=800:
        num_cards = int(pos[0] / 50) + 1
        # print num_cards
        if state == 0 and (card[num_cards] !=0):
            state =1
        elif state ==1 and (card[num_cards] !=0):
            state =2
            steps = steps+1
        elif (state ==2) and (num1 != num2) and (card[num_cards] !=0):
            state = 1
            card[num_cards1+1] = num_cards1+1
            card[num_cards2+1] = num_cards2+1
        elif (state ==2) and (num1 == num2) and (card[num_cards] !=0):
            state = 1
    elif pos[0] >800 and pos[1] <=50:
        init()

def drawing():
    global card, num1, num2,num_cards1, num_cards2,steps,image
    if state == 1 and (card[num_cards] !=0):
        num1=x[num_cards-1]
        num_cards1 = num_cards - 1
        card[num_cards] = 0
    elif state ==2 and (card[num_cards] !=0):
        num2=x[num_cards-1]
        num_cards2 = num_cards -1
        card[num_cards] = 0
init()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            key_x, key_y = pygame.mouse.get_pos()
            pos = [key_x, key_y]
            mouseclick(pos)
    drawing()
    i = 0
    j = 0
    screen.fill([0,0,0])
    for item in x:
        ##font = pygame.font.Font(None, 60)
        text.append( font.render(str(item),0,(255,255,255)))
        screen.blit(text[j],(10+i, 25))
        j = j+1
        i = i+50
        
    for num in card:
        if num:
            screen.lock()
            pygame.draw.line(screen,(255,255,0), (25+(num-1)*50,0), (25+(num-1)*50, 100), 49)
            screen.unlock()
    screen.lock()
    pygame.draw.line(screen,(255,34,111),(850,0),(850,50),99)
    pygame.draw.line(screen,(132,231,42),(850,51),(850,100),99)
    screen.unlock()
    screen.blit( font3.render("Restart", 0,(0,0,0)), (808,9))
    screen.blit( font2.render("Steps: "+str(steps),0,(0,0,0)), (810,65))
    pygame.display.update()





