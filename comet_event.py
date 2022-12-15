import pygame

class CometFallEvent:

    def __init__(self):
        self.percent = 0
        self.percent_speed = 5

    def add_percent(self):
        self.percent += self.percent_speed / 200
    
    def update_bar(self, surface):
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