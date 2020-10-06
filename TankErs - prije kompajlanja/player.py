import pygame

#PLAYERS
class Player():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.x = 0
        self.y = 0
        if name == "1":
            self.sprite = pygame.image.load("graphics/player1.png")
        if name == "2":
            self.sprite = pygame.image.load("graphics/player2.png")

    def position(self,new_x,new_y):
        self.x += new_x
        self.y += new_y

    def damaged(self,hit):
        if hit == True:
            self.health -= 100

#PLAYERS
player_1 = Player("1")
player_2 =  Player("2")