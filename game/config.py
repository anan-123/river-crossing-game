import pygame
from pygame.locals import *
pygame.init()
# colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
FONT = pygame.font.SysFont('comicsans', 50, True)

# initial coordinates of moving obstacles
X_1 = 0
X_2 = 1400
X_3 = 865
X_4 = 345
X_5 = 765

TURN = 1
LEVEL = 0

# initial coordinates of player1
X1 = 0
Y1 = 939

# initial coordinates of player2
X2 = 1729
Y2 = 89

# initialize score
P1SCORE = 0


def score1():
    global P1SCORE
    P1SCORE = 0


# initialize score
P2SCORE = 0


def score2():
    global P2SCORE
    P2SCORE = 0


score1()
score2()

# detecting collisions for players

COLLIDE1 = 0
COLLIDE2 = 0

SLAB = 1
SPEED = 5
i = 0
j = 0
t1 = 0
t2 = 0