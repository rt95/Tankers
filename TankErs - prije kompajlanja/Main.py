import pygame,sys,time
from pygame.locals import *
from player import *
from colors import *
from settings import *
from tkinter import *

#INITIALIZE PYGAME MODULES
pygame.init()

#CLOCK
clock = pygame.time.Clock()

#FPS
currentSec = 0
currentFrame = 0
FPS = 0
deltatime = 0

#FONTS
font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
score_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 40)

#LOAD IMAGES
icon = pygame.image.load("graphics/icon.png")
pygame.display.set_icon(icon)
player_1_tank = player_1.sprite
player_2_tank = player_2.sprite
player_1_tank_image_size = player_1_tank.get_rect().size
player_2_tank_image_size = player_2_tank.get_rect().size
ground = pygame.image.load("graphics/ground.png")
wall = pygame.image.load("graphics/wall.png")
player_1_bullet = pygame.image.load("graphics/bullet.png")
player_2_bullet = pygame.image.load("graphics/bullet.png")
bullet_clear = pygame.image.load("graphics/bullet_clear.png")

#MASKING
wall_mask = pygame.mask.from_surface(wall)
player_1_tank_mask = pygame.mask.from_surface(player_1_tank)
player_2_tank_mask = pygame.mask.from_surface(player_2_tank)
player_1_bullet_mask = pygame.mask.from_surface(player_1_bullet)
player_2_bullet_mask = pygame.mask.from_surface(player_2_bullet)

#PLAYER 1
player_1_xPos = player_1.x
player_1_yPos = player_1.y
player_1_tank_move = 0

#PLAYER 2
player_2_xPos = player_2.x
player_2_yPos = player_2.y
player_2_tank_move = 0

#SHOOTING
#PLAYER 1
player_1_shot = False
player_1_bullet_move = 0

#PLAYER 2
player_2_shot = False
player_2_bullet_move = 0

#DEFINE FPS CALCULATIONS
def count_fps():
    global currentSec, currentFrame, FPS, deltatime

    if currentSec == time.strftime("%S"):
        currentFrame += 1
    else:
        FPS = currentFrame
        currentFrame = 0
        currentSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS

#SHOW FPS
def show_fps():
    fps_overlay = font.render("FPS:" + str(FPS), True, orange) #True = Antialiasing
    screen.blit(fps_overlay,(5,5))

#SHOW TANK POSITION
def show_tankPos():
    tankPos_x = font.render("Tank X pos:{0:.2f}".format(player_1_xPos), True, orange)  # True = Antialiasing
    tankPos_y = font.render("Tank Y pos:{0:.2f}".format(player_1_yPos), True, orange)  # True = Antialiasing
    screen.blit(tankPos_x, (5, 50))
    screen.blit(tankPos_y, (5, 80))

#SHOW SCORE
player_1_score = 0
player_2_score = 0

def show_score():
    player_1_score_render = score_font.render("{}".format(player_1_score),True, orange)
    player_2_score_render = score_font.render("{}".format(player_2_score), True, orange)
    if player_1_score < 9 or player_2_score < 9:
        screen.blit(player_1_score_render, (410, 5))
        screen.blit(player_2_score_render, (300, 5))
    if player_2_score > 9:
        screen.blit(player_1_score_render, (410, 5))
        screen.blit(player_2_score_render, (274, 5))

#WHILE THE GAME IS RUNNING
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == KEYDOWN:

            ##SHOOTING
            if event.key == pygame.K_RCTRL:
                player_1_shot = True
                player_1_bullet_move = 1
            if event.key == pygame.K_SPACE:
                player_2_shot = True
                player_2_bullet_move = 1

        if event.type == KEYUP:
            player_1_tank_move = 0
            player_2_tank_move = 0

    ##TANK MOVEMENT
    key = pygame.key.get_pressed()

    if key[K_UP]:
        player_1_yPos -= 200 * deltatime
    if key[K_DOWN]:
        player_1_yPos += 200 * deltatime
    if key[K_LEFT]:
        player_1_xPos -= 200 * deltatime
    if key[K_RIGHT]:
        player_1_xPos += 200 * deltatime

    ##CAMERA MOVEMENT & PLAYER 2
    if key[K_w]:
        player_2_yPos -= 200 * deltatime
    if key[K_s]:
        player_2_yPos += 200 * deltatime
    if key[K_a]:
        player_2_xPos -= 200 * deltatime
    if key[K_d]:
        player_2_xPos += 200 * deltatime

    if player_1_bullet_move == 0:
        player_1_BulletX = player_1_xPos - 10 #-10 is bullet image width in pixels
        player_1_BulletY = player_1_yPos + player_1_tank_image_size[1] / 2 - 1

    if player_1_bullet_move == 1:
        player_1_BulletX -= 15
        player_1_BulletY += 0

    if player_2_bullet_move == 0:
        player_2_BulletX = player_2_xPos + player_2_tank_image_size[0]
        player_2_BulletY = player_2_yPos + player_2_tank_image_size[1] / 2 - 1

    if player_2_bullet_move == 1:
        player_2_BulletX += 15
        player_2_BulletY += 0


    #FILL BACKGROUND WITH BLACK COLOR
    screen.fill(black)

    #BLIT THE SURFACE
    surface = pygame.Surface((32,32)) #Width, Height of surface tile
    surface.blit(ground, (0, 0))

    #RENDER SIMPLE TERRAIN GRID
    for x in range(0,windowWidth,32):
        for y in range(0,windowHeight,32):
            screen.blit(surface, (x,y))

    #RENDER THE TANK
    #PLAYER 1
    screen.blit(player_1_tank, (player_1_xPos,player_1_yPos))
    #PLAYER 2
    screen.blit(player_2_tank, (player_2_xPos, player_2_yPos))

    #MASKING
    player_1_xPos_mask,player_1_yPos_mask = player_1_xPos, player_1_yPos
    player_2_xPos_mask, player_2_yPos_mask = player_2_xPos, player_2_yPos

    #WALLS
    for y_1 in range(0,windowHeight,64):
        for x_1 in range(windowWidth // 2,windowWidth // 2 + 32,32):
            walls_x_pos, walls_y_pos = x_1, y_1
            screen.blit(wall, (x_1, y_1))

        #TANK COLLISIONS
        offset_player_1 = (int(player_1_xPos_mask - walls_x_pos), int(player_1_yPos_mask - walls_y_pos))
        offset_player_2 = (int(player_2_xPos_mask - walls_x_pos), int(player_2_yPos_mask - walls_y_pos))
        player_1_tank_hits_wall = wall_mask.overlap(player_1_tank_mask, offset_player_1)
        player_2_tank_hits_wall = wall_mask.overlap(player_2_tank_mask, offset_player_2)

        if player_1_tank_hits_wall:
            player_1_xPos = player_1_xPos + 5

        if player_2_tank_hits_wall:
            player_2_xPos = player_2_xPos - 5

        #CANT CROSS MIDDLE

        if player_1_xPos < windowWidth / 2 + 32: #32 is wall pixel width
            player_1_xPos = player_1_xPos + 5

        if player_2_xPos > windowWidth / 2 - player_2_tank_image_size[0]:
            player_2_xPos = player_2_xPos - 5

        #CANT GO OUT OF BOUNDS
        #PLAYER 1
            #X POS
        if player_1_xPos > windowWidth - player_1_tank_image_size[0]:
            player_1_xPos = player_1_xPos - 5
            #Y POS BOTTOM
        if player_1_yPos > windowHeight - player_1_tank_image_size[1]:
            player_1_yPos = player_1_yPos - 5
            #Y POS TOP
        if player_1_yPos < 0:
            player_1_yPos = player_1_yPos + 5

        #PLAYER 2
            #X POS
        if player_2_xPos < 0:
            player_2_xPos = player_2_xPos + 5
            #Y POS BOTTOM
        if player_2_yPos > windowHeight - player_2_tank_image_size[1]:
            player_2_yPos = player_2_yPos - 5
            #Y POS TOP
        if player_2_yPos < 0:
            player_2_yPos = player_2_yPos + 5

        #BULLET COLLISION
        #PLAYER 1
        player_1_bullet_x_pos, player_1_bullet_y_pos = player_1_BulletX, player_1_BulletY
            #WALL HIT
        player_1_bullet_offset = (int(player_1_bullet_x_pos - walls_x_pos), int(player_1_bullet_y_pos - walls_y_pos))
        player_1_bullet_hits_wall = wall_mask.overlap(player_1_bullet_mask, player_1_bullet_offset)
            #PLAYER HIT
        player_1_hit_offset = (int(player_1_bullet_x_pos - player_2_xPos_mask), int(player_1_bullet_y_pos - player_2_yPos_mask))
        player_1_bullet_hits_player_2 = player_2_tank_mask.overlap(player_1_bullet_mask, player_1_hit_offset)

        #PLAYER 2
        player_2_bullet_x_pos, player_2_bullet_y_pos = player_2_BulletX, player_2_BulletY
            #WALL HIT
        player_2_bullet_offset = (int(player_2_bullet_x_pos - walls_x_pos), int(player_2_bullet_y_pos - walls_y_pos))
        player_2_bullet_hits_wall = wall_mask.overlap(player_2_bullet_mask, player_2_bullet_offset)
            #PLAYER HIT
        player_2_hit_offset = (int(player_2_bullet_x_pos - player_1_xPos_mask), int(player_2_bullet_y_pos - player_1_yPos_mask))
        player_2_bullet_hits_player_1 = player_1_tank_mask.overlap(player_2_bullet_mask, player_2_hit_offset)

        #RENDER BULLETS
        #PLAYER 1
        if player_1_shot == True:
            screen.blit(player_1_bullet, (player_1_BulletX, player_1_BulletY))
            if player_1_BulletX < 0:
                player_1_bullet_move = 0
                screen.blit(bullet_clear, (player_1_BulletX, player_1_BulletY))
                player_1_BulletX = player_1_xPos
                player_1_BulletY = player_1_yPos
                player_1_shot = False
            if player_1_bullet_hits_wall:
                player_1_bullet_move = 0
                screen.blit(bullet_clear,(player_1_BulletX,player_1_BulletY))
                player_1_BulletX = player_1_xPos
                player_1_BulletY = player_1_yPos
                player_1_shot = False
            if player_1_bullet_hits_player_2:
                player_1_bullet_move = 0
                screen.blit(bullet_clear, (player_1_BulletX, player_1_BulletY))
                player_1_BulletX = player_1_xPos
                player_1_BulletY = player_1_yPos
                player_1_shot = False
                player_2.damaged(True)

        #PLAYER 2
        if player_2_shot == True:
            screen.blit(player_2_bullet, (player_2_BulletX, player_2_BulletY))
            if player_2_BulletX > windowWidth:
                player_2_bullet_move = 0
                screen.blit(bullet_clear, (player_2_BulletX, player_2_BulletY))
                player_2_BulletX = player_2_xPos
                player_2_BulletY = player_2_yPos
                player_2_shot = False
            if player_2_bullet_hits_wall:
                player_2_bullet_move = 0
                screen.blit(bullet_clear, (player_2_BulletX, player_2_BulletY))
                player_2_BulletX = player_2_xPos
                player_2_BulletY = player_2_yPos
                player_2_shot = False
            if player_2_bullet_hits_player_1:
                player_2_bullet_move = 0
                screen.blit(bullet_clear, (player_2_BulletX, player_2_BulletY))
                player_2_BulletX = player_2_xPos
                player_2_BulletY = player_2_yPos
                player_2_shot = False
                player_1.damaged(True)


    ###
    clock.tick(60)
    #show_fps()
    #show_tankPos()
    show_score()
    pygame.display.update()
    count_fps()

    if player_2.health == 0:
        player_2.health = 100
        player_1_score += 1

    if player_1.health == 0:
        player_1.health = 100
        player_2_score += 1
    ###

pygame.quit()
sys.exit()