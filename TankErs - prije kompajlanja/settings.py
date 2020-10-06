import pygame
from player import *

#SCREEN WIDTH AND HEIGHT
windowWidth = 704
windowHeight = 352

#RENDER SCREEN WIDTH AND HEIGHT
screen = pygame.display.set_mode((windowWidth,windowHeight),pygame.HWSURFACE|pygame.DOUBLEBUF)

pygame.display.set_caption("TankErs")

#TANK START POSITIONS DECLARATION
player_1.position(600,195)
player_2.position(50,130)

scene = "GUI"