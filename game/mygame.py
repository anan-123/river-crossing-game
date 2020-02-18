# imorting modules
import pygame
import sys
from pygame.locals import *
from config import *
pygame.init()

# setting screen
DISPLAYSURF = pygame.display.set_mode((1830, 1010))

# setting background image
BGIMG = pygame.image.load("gamebackground.jpg")
BGIMG = pygame.transform.scale(BGIMG, (1830, 1010))

# moving obstacles fetching images
SH1 = pygame.image.load("s1.jpeg")
SH1 = pygame.transform.scale(SH1, (100, 100))
SH2 = pygame.image.load("s2.jpeg")
SH2 = pygame.transform.scale(SH2, (100, 100))
SH3 = pygame.image.load("s3.jpeg")
SH3 = pygame.transform.scale(SH3, (100, 100))
SH4 = pygame.image.load("s4.jpeg")
SH4 = pygame.transform.scale(SH4, (100, 100))
SH5 = pygame.image.load("s5.jpeg")
SH5 = pygame.transform.scale(SH5, (100, 100))

# caption
pygame.display.set_caption('river crossing battle')

# setting background image
DISPLAYSURF.blit(BGIMG, (0, 0))

# drawing the SLABs


def createSLAB():
    pygame.draw.rect(DISPLAYSURF, BLUE, (0, 939, 1830, 70))
    pygame.draw.rect(DISPLAYSURF, BLUE, (0, 769, 1830, 70))
    pygame.draw.rect(DISPLAYSURF, BLUE, (0, 599, 1830, 70))
    pygame.draw.rect(DISPLAYSURF, BLUE, (0, 429, 1830, 70))
    pygame.draw.rect(DISPLAYSURF, BLUE, (0, 259, 1830, 70))
    pygame.draw.rect(DISPLAYSURF, BLUE, (0, 89, 1830, 70))
    pygame.draw.rect(DISPLAYSURF, GREEN, (0, 0, 1830, 90))


createSLAB()

# stationary obstacles


def stationaryobstacles():
    pygame.draw.rect(DISPLAYSURF, SILVER, (935, 939, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (450, 769, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (1365, 769, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (915, 599, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (746, 429, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (1500, 429, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (0, 259, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (1100, 259, 100, 70))
    pygame.draw.rect(DISPLAYSURF, SILVER, (567, 89, 100, 70))


stationaryobstacles()

def initmov(I):
    global X_1
    global X_2
    global X_3
    global X_4
    global X_5

    X_1 = X_1 + I
    if X_1 <= 1729:
        POSITION = pygame.Rect(X_1, 839, 100, 100)
    else:
        X_1 = 0
        POSITION = pygame.Rect(X_1, 839, 100, 100)
    DISPLAYSURF.blit(SH1, POSITION)
    X_2 = X_2 + I
    if X_2 <= 1729:
        POSITION = pygame.Rect(X_2, 669, 100, 100)
    else:
        X_2 = 0
        POSITION = pygame.Rect(X_2, 669, 100, 100)
    DISPLAYSURF.blit(SH2, POSITION)
    X_3 = X_3 + I
    if X_3 <= 1729:
        POSITION = pygame.Rect(X_3, 499, 100, 100)
    else:
        X_3 = 0
        POSITION = pygame.Rect(X_3, 499, 100, 100)
    DISPLAYSURF.blit(SH3, POSITION)
    X_4 = X_4 + I
    if X_4 <= 1729:
        POSITION = pygame.Rect(X_4, 329, 100, 100)
    else:
        X_4 = 0
        POSITION = pygame.Rect(X_4, 329, 100, 100)
    DISPLAYSURF.blit(SH4, POSITION)
    X_5 = X_5+I
    if X_5 <= 1729:
        POSITION = pygame.Rect(X_5, 159, 100, 100)
    else:
        X_5 = 0
        POSITION = pygame.Rect(X_5, 159, 100, 100)
    DISPLAYSURF.blit(SH5, POSITION)

# getting image for player 1 and player 2
PLAY1IMG = pygame.image.load('cat2.png')
POSITION = pygame.Rect(X1, Y1, 100, 200)
PLAY2IMG = pygame.image.load('cat2.png')
POSITION = pygame.Rect(X2, Y2, 100, 200)
if TURN == 1:
    DISPLAYSURF.blit(PLAY1IMG, POSITION)
if TURN == 2:
    DISPLAYSURF.blit(PLAY2IMG, POSITION)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def collisiondetection1():
    # static collision
    global COLLIDE1
    if X1 > 935-100 and X1 < 935+100:
        if Y1 < 939+70 and Y1 > 939-70:
            COLLIDE1 = 1
    if X1 > 450-100 and X1 < 450+100:
        if Y1 < 769+70 and Y1 > 769-70:
            COLLIDE1 = 1
    if X1 > 1365-100 and X1 < 1365+100:
        if Y1 < 769+70 and Y1 > 769-70:
            COLLIDE1 = 1
    if X1 > 915-100 and X1 < 915+100:
        if Y1 < 599+70 and Y1 > 599-70:
            COLLIDE1 = 1
    if X1 > 746-100 and X1 < 746+100:
        if Y1 < 429+70 and Y1 > 429-70:
            COLLIDE1 = 1
    if X1 > 1500-100 and X1 < 1500+100:
        if Y1 < 429+70 and Y1 > 429-70:
            COLLIDE1 = 1
    if X1 > 0-100 and X1 < 0+100:
        if Y1 < 259+70 and Y1 > 259-70:
            COLLIDE1 = 1
    if X1 > 1100-100 and X1 < 1100+100:
        if Y1 < 259+70 and Y1 > 259-70:
            COLLIDE1 = 1
    if X1 > 567-100 and X1 < 567+100:
        if Y1 < 89+70 and Y1 > 89-70:
            COLLIDE1 = 1
# moving obstacles collision
    if X1 > X_1-100 and X1 < X_1+100:
        if Y1 < 839+70 and Y1 > 839-70:
            COLLIDE1 = 1
    if X1 > X_2-100 and X1 < X_2+100:
        if Y1 < 669+70 and Y1 > 669-70:
            COLLIDE1 = 1
    if X1 > X_3-100 and X1 < X_3+100:
        if Y1 < 499+70 and Y1 > 499-70:
            COLLIDE1 = 1
    if X1 > X_4-100 and X1 < X_4+100:
        if Y1 < 329+70 and Y1 > 329-70:
            COLLIDE1 = 1
    if X1 > X_5-100 and X1 < X_5+100:
        if Y1 < 159+70 and Y1 > 159-70:
            COLLIDE1 = 1


# collision detection for player 2
def collisiondetection2():

    global COLLIDE2
    '''if x2 > 935-100 and x2 < 935+100:
  if y2 < 939+70 and y2 > 939-70:
    font = pygame.font.SysFont('comicsans', 50, True)
    COLLIDE2 = 1'''

    if X2 > 935-100 and X2 < 935+100:
        if Y2 < 939+70 and Y2 > 939-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
           # DISPLAYSURF.blit(text, (915, 500))

    if X2 > 1365-100 and X2 < 1365+100:
        if Y2 < 769+70 and Y2 > 769-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > 915-100 and X2 < 915+100:
        if Y2 < 599+70 and Y2 > 599-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > 746-100 and X2 < 746+100:
        if Y2 < 429+70 and Y2 > 429-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > 1500-100 and X2 < 1500+100:
        if Y2 < 429+70 and Y2 > 429-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > 0-100 and X2 < 0+100:
        if Y2 < 259+70 and Y2 > 259-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > 1100-100 and X2 < 1100+100:
        if Y2 < 259+70 and Y2 > 259-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > 567-100 and X2 < 567+100:
        if Y2 < 89+70 and Y2 > 89-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
# moving obstacles collision
    if X2 > X_1-100 and X2 < X_1+100:
        if Y2 < 839+70 and Y2 > 839-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > X_2-100 and X2 < X_2+100:
        if Y2 < 669+70 and Y2 > 669-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > X_3-100 and X2 < X_3+100:
        if Y2 < 499+70 and Y2 > 499-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > X_4-100 and X2 < X_4+100:
        if Y2 < 329+70 and Y2 > 329-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))
    if X2 > X_5-100 and X2 < X_5+100:
        if Y2 < 159+70 and Y2 > 159-70:
            #font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
            #DISPLAYSURF.blit(text, (915, 500))


def press():
    global X1
    global Y1
    global P1SCORE
    global SLAB
    if pressed[pygame.K_UP] and Y1 > 98:
        Y1 -= 85
        if SLAB % 2 != 0:
            P1SCORE += 5
        else:
            P1SCORE += 10
        SLAB += 1
    if pressed[pygame.K_DOWN] and Y1 < 1010-100-2+25:
        Y1 += 85
        if SLAB % 2 != 0:
            P1SCORE -= 13
        else:
            P1SCORE -= 8
        SLAB -= 1
    if pressed[pygame.K_LEFT] and X1 > 2:
        X1 -= 85
    if pressed[pygame.K_RIGHT] and X1 < 1830-100-2+25:
        X1 += 85


def press2():
    global X2
    global Y2
    global P2SCORE
    global SLAB
    if pressed[pygame.K_UP] and Y2 > 98:
        Y2 -= 85
        if SLAB % 2 != 0:
            P2SCORE -= 13
        else:
            P2SCORE -= 8
        SLAB += 1
    if pressed[pygame.K_DOWN] and Y2 < 1010-100-2+25:
        Y2 += 85
        if SLAB % 2 != 0:
            P2SCORE += 10
        else:
            P2SCORE += 5
        SLAB -= 1
    if pressed[pygame.K_LEFT] and X2 > 102:
        X2 -= 85
    if pressed[pygame.K_RIGHT] and X2 < 1830-100-2+25-100:
        X2 += 85


# Hide the mouse cursor
pygame.mouse.set_visible(0)

# the main game loop
def finishlevel():
    global P1SCORE
    global P2SCORE
    global t1
    global t2
    if P1SCORE > P2SCORE:
        font = pygame.font.SysFont('comicsans', 150, True)
        text = font.render('PLAYER1 WON THE GAME!', 1, (255, 255, 255))
        DISPLAYSURF.blit(BGIMG, (0, 0))
        DISPLAYSURF.blit(text, (300, 500))
        pygame.display.flip()
        pygame.time.delay(2000)
    elif P2SCORE > P1SCORE:
        font = pygame.font.SysFont('comicsans', 150, True)
        text = font.render('PLAYER2 WON THE GAME!', 1, (255, 255, 255))
        DISPLAYSURF.blit(BGIMG, (0, 0))
        DISPLAYSURF.blit(text, (300, 500))
        pygame.display.flip()
        pygame.time.delay(2000)
    else:
        if t2 > t1:
            font = pygame.font.SysFont('comicsans', 150, True)
            text = font.render('PLAYER1 WON THE GAME!', 1, (255, 255, 255))
            DISPLAYSURF.blit(BGIMG, (0, 0))
            DISPLAYSURF.blit(text, (300, 500))
            pygame.display.flip()
            pygame.time.delay(2000)
        if t1 > t2:
            font = pygame.font.SysFont('comicsans', 150, True)
            text = font.render('PLAYER2 WON THE GAME!', 1, (255, 255, 255))
            DISPLAYSURF.blit(BGIMG, (0, 0))
            DISPLAYSURF.blit(text, (300, 500))
            pygame.display.flip()
            pygame.time.delay(2000)
        if t1 == t2:
            font = pygame.font.SysFont('comicsans', 150, True)
            text = font.render('IT IS A DRAW!', 1, (255, 255, 255))
            DISPLAYSURF.blit(BGIMG, (0, 0))
            DISPLAYSURF.blit(text, (300, 500))
            pygame.display.flip()
            pygame.time.delay(2000)


while True:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if TURN == 1:
            press()
        else:
            press2()

    DISPLAYSURF.blit(BGIMG, (0, 0))
    createSLAB()
    if TURN == 1:
        font = pygame.font.SysFont('comicsans', 70, True)
        text = font.render('START', 1, (255, 255, 255))
        DISPLAYSURF.blit(text, (0, 939))
        font = pygame.font.SysFont('comicsans', 70, True)
        text = font.render('END', 1, (255, 255, 255))
        DISPLAYSURF.blit(text, (1700, 100))
    if TURN == 2:
        font = pygame.font.SysFont('comicsans', 60, True)
        text = font.render('START', 1, (255, 255, 255))
        DISPLAYSURF.blit(text, (1700, 100))
        font = pygame.font.SysFont('comicsans', 60, True)
        text = font.render('END', 1, (255, 255, 255))
        DISPLAYSURF.blit(text, (0, 939))

    stationaryobstacles()
    initmov(SPEED)

    if TURN == 1:
        POSITION = pygame.Rect(X1, Y1, 100, 200)
        DISPLAYSURF.blit(PLAY1IMG, POSITION)

    if TURN == 2:
        POSITION = pygame.Rect(X2, Y2, 100, 200)
        DISPLAYSURF.blit(PLAY2IMG, POSITION)

    font = pygame.font.SysFont('comicsans', 60, True)
    text = font.render('Player 1 : '+str(P1SCORE), 1, (0, 0, 0))
    DISPLAYSURF.blit(text, (121, 25))

    font = pygame.font.SysFont('comicsans', 60, True)
    text = font.render('Player 2 : '+str(P2SCORE), 1, (0, 0, 0))
    DISPLAYSURF.blit(text, (500, 25))
    font = pygame.font.SysFont('comicsans', 60, True)
    text = font.render('Level : '+str(LEVEL), 1, (0, 0, 0))
    DISPLAYSURF.blit(text, (850, 25))
    if TURN == 1:
        t1 = i/40
    else:
        t2 = j/40
    font = pygame.font.SysFont('comicsans', 60, True)
    text = font.render('Timer1 : '+str(t1), 1, (0, 0, 0))
    DISPLAYSURF.blit(text, (1210, 25))

    font = pygame.font.SysFont('comicsans', 60, True)
    text = font.render('Timer2 : '+str(t2), 1, (0, 0, 0))
    DISPLAYSURF.blit(text, (1500, 25))

    collisiondetection1()
    if COLLIDE1 == 1:
        X1 = 0
        Y1 = 939
        SLAB = 1
        TURN = 2
        COLLIDE1 = 0
    collisiondetection2()
    if X2 > 450-100 and X2 < 450+100:
        if Y2 < 769+70 and Y2 > 769-70:
            font = pygame.font.SysFont('comicsans', 50, True)
            COLLIDE2 = 1
    if COLLIDE2 == 1:
        X2 = 1729
        Y2 = 89
        SLAB = 1
        finishlevel()
        TURN = 1
        COLLIDE2 = 0
    if TURN == 1:
        i = i+1
    else:
        j = j+1
    if X1 >= 1829-130 and Y1 == 89:
        X1 = 0
        Y1 = 939
        SLAB = 1
        TURN = 2
    if X2 <= 104 and Y2 == 1009-70:
        SPEED += 4
        X2 = 1729
        Y2 = 89
        SLAB = 1
        finishlevel()
        TURN = 1
        LEVEL += 1

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
