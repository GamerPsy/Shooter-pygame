import pygame
from player import Player

#creation classe game
class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}
