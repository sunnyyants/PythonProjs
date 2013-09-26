# Implement the Pond Game!!

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
score1 = 0
score2 = 0
bif="/Users/SunnyYan/Dropbox/Codings/Python Projects/PondGame/background.jpg"
mif="/Users/SunnyYan/Dropbox/Codings/Python Projects/PondGame/ball.png"
pif = "/Users/SunnyYan/Dropbox/Codings/Python Projects/PondGame/pad.jpg"

import random
import math
import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600,400), 0, 32)
pygame.display.set_caption("The Pond Game")
background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()
pad1 = pygame.image.load(pif).convert()
pad2 = pygame.image.load(pif).convert()
font = pygame.font.Font(None,50)
font2 = pygame.font.Font(None, 60)
font3 = pygame.font.Font(None, 30)


def ball_init(right):
    global ball_pos, ball_vel, clock,clock2 ,time
    ball_pos = [(WIDTH - ball.get_width()) / 2, (HEIGHT - ball.get_height()) / 2]
    if right:
        balldir = 1
    else:
        balldir = -1
    ball_vel = [random.randrange(120,240), random.randrange(60,180)]
    ball_vel[0] = ball_vel[0] * balldir
    clock = pygame.time.Clock()
    clock2 = pygame.time.Clock()
    time=1000.0

def ball_moving():
    global clock, ball_pos, ball_vel, time, score1, score2
    milli = clock.tick()
    seconds = milli /time
    ball_pos[0] += ball_vel[0] * seconds
    ball_pos[1] += ball_vel[1] * seconds
    
    if ((ball_pos[0]>600-(ball.get_width()+PAD_WIDTH)) and math.fabs(ball_pos[1] - pad2_pos[1]) <= ball.get_height()) :
        ball_vel[0] = -(ball_vel[0])
        time = time*0.85
        
    elif ((ball_pos[0]>600-(ball.get_width()+PAD_WIDTH)) and math.fabs(ball_pos[1] - pad2_pos[1]) > ball.get_height()) :
        score1 +=1
        ball_init(0)
        
    elif (ball_pos[0]<PAD_WIDTH and math.fabs(ball_pos[1] - pad1_pos[1]) <= ball.get_height()):
        ball_vel[0] = -(ball_vel[0])
        time = time*0.85
        
    elif (ball_pos[0]<PAD_WIDTH and math.fabs(ball_pos[1] - pad1_pos[1]) > ball.get_height()):
        score2 +=1
        ball_init(1)
        
    elif (ball_pos[1]>400-ball.get_width()) or (ball_pos[1]<0): 
        ball_vel[1] = -ball_vel[1]



def pads_init():
    global pad1_pos, pad2_pos, pad1_vel, pad2_vel
    pad1_pos = [0, (HEIGHT - pad1.get_height()) / 2]
    pad2_pos = [WIDTH -PAD_WIDTH, (HEIGHT - pad2.get_height()) / 2]
    pad1_vel = [0,0]
    pad2_vel = [0,0]

def pads_moving():
    global pad1_pos, pad2_pos, pad1_vel, pad2_vel

    pad1_pos[1] += pad1_vel[1]
    pad2_pos[1] += pad2_vel[1]

    if(pad1_pos[1] <= 0):
        pad1_pos[1] = 0
    elif (pad1_pos[1] >= HEIGHT-pad1.get_height()):
        pad1_pos[1] = HEIGHT-pad1.get_height()
    if(pad2_pos[1] <= 0):
        pad2_pos[1] = 0
    elif (pad2_pos[1] >= HEIGHT-pad2.get_height()):
        pad2_pos[1] = HEIGHT-pad2.get_height()

def new_game():
    global score1, score2
    ball_init(0)
    pads_init()
    score1 = 0
    score2 =0

ball_init(1)
pads_init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                pad2_vel[1] += 5
            if event.key == K_UP:
                pad2_vel[1] -= 5
            if event.key == K_s:
                pad1_vel[1] += 5
            if event.key == K_w:
                pad1_vel[1] -= 5
        if event.type ==KEYUP:
            if event.key == K_DOWN:
                pad2_vel[1] -= 5
            if event.key == K_UP:
                pad2_vel[1] += 5
            if event.key == K_s:
                pad1_vel[1] -= 5
            if event.key == K_w:
                pad1_vel[1] += 5
        if event.type ==MOUSEBUTTONDOWN:
            new_game()
            
            
    screen.blit(background, (0,0))
    screen.lock()
    pygame.draw.line(screen,(255,0,0),(WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 2)
    pygame.draw.line(screen,(255,0,0),(PAD_WIDTH, 0), (PAD_WIDTH, HEIGHT), 2)
    pygame.draw.line(screen,(255,0,0),(WIDTH - PAD_WIDTH, 0), (WIDTH - PAD_WIDTH, HEIGHT), 2)
    screen.unlock()
    text = font.render(str(score1) + "      " +str(score2), 4,(255,0,0))
    text2= font2.render("The Pond Game", 5, (255,255,255))
    text3 = font3.render("Click any place to restart...", 5,(255,255,255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    screen.blit(text,textpos)
    screen.blit(text2,(150,300))
    screen.blit(text3,(180,350))
    screen.blit(ball,(ball_pos[0], ball_pos[1]))
    screen.blit(pad1, (pad1_pos[0], pad1_pos[1]))
    screen.blit(pad2, (pad2_pos[0], pad2_pos[1]))

    ball_moving()
    pads_moving()
    pygame.display.update()    





        
