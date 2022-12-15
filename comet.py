import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_vent):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0,800)
        self.comet_vent = comet_vent

    def remove(self):
        self.comet_vent.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            print("sol")
            self.remove()

        if self.comet_vent.game.check_collision(self, self.comet_vent.game.all_players):
            print("Joueur touché")
            self.remove()
            self.comet_vent.game.player.damage(20)