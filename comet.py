import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_vent):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_vent

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.soundManager.play("meteorite")
        if len(self.comet_event.all_comets) == 0:
            #print("pluie finie")
            self.comet_event.reset_percent()
            self.comet_event.game.start()
            

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            #print("sol")
            self.remove()

        if len(self.comet_event.all_comets) == 0:
            #print("eventement fini")
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #print("Joueur touché")
            self.remove()
            self.comet_event.game.player.damage(20)
