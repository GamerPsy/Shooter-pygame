import pygame
from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent

#creation classe game
class Game:

    def __init__(self):
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.comet_vent = CometFallEvent(self)

        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)


    def game_over(self):
        #remettre le jeu à zero : retirer les monstres, remettre le hero à fond en pv, mettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_vent.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_vent.reset_percent()
        self.is_playing = False


    def update(self, screen):
        #appliquer image du joueur
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        self.comet_vent.update_bar(screen)

        self.player.update_animation()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_vent.all_comets:
            comet.fall()
        #appliquer ensemble images projectiles
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.comet_vent.all_comets.draw(screen)

        #gestion mouvement joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x  + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self, monster_name):
        self.all_monsters.add(monster_name.__call__(self))
