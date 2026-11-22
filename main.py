

import pygame
import sys
import random as ran
from pygame.locals import *

# global variables
FPS = 30
SCREENWIDTH = 289
SCREENHEIGHT = 511
#SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = 0.8
GAME_AUDIO = {}
GAME_SPRITES = {}
PLAYER = './assets/sprites/yellowbird-midflap.png'
BACKGROUND = './assets/sprites/background-night.png'
PIPE = './assets/sprites/pipe-green.png'


def welcomeScreen():
    """
    Shows welcome screen w images n shi
    """
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int(SCREENWIDTH - GAME_SPRITES['message'].get_width())/2
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0

    while True:
        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0,0))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    basex = 0

# blitting pipes
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

def getRandomPipe():




if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    bg = pygame.image.load(BACKGROUND)
    SCREENWIDTH, SCREENHEIGHT = bg.get_size()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT*0.8




    GAME_SPRITES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha(),

    )
    GAME_SPRITES['message'] = pygame.image.load('assets/sprites/message.png').convert_alpha()
    GAME_SPRITES['pipe'] =(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha(),
    )
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()



    GAME_AUDIO['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh.wav')
    GAME_AUDIO['wing'] = pygame.mixer.Sound('assets/audio/wing.wav')
    GAME_AUDIO['point'] = pygame.mixer.Sound('assets/audio/point.wav')
    GAME_AUDIO['hit'] = pygame.mixer.Sound('assets/audio/hit.wav')
    GAME_AUDIO['die'] = pygame.mixer.Sound('assets/audio/die.wav')



    while True:
        welcomeScreen()
        #mainGame()
