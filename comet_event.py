import pygame
from comet import Comet

class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.all_comets = pygame.sprite.Group()
        self.game = game

    def add_percent(self):
        self.percent += self.percent_speed / 200

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded():
            print("pluie de comètes")
            self.meteor_fall()
            self.reset_percent()
    
    def update_bar(self, surface):
        self.attempt_fall()

        self.add_percent()
        # barre arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe des x
            surface.get_height() - 10, # axe des y
            surface.get_width(), # largeur écran
            10 # épaisseur de la barrre de chargement event
        ])
        # barre chargement event
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # axe des x
            surface.get_height() - 10, # axe des y
            (surface.get_width() / 100) * self.percent, # largeur écran
            10 # épaisseur de la barrre de chargement event
        ])