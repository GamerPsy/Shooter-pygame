import pygame
from player import Player
from monster import Monster

#creation classe game
class Game:

    def __init__(self):
        self.is_playing = False

        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remettre le jeu à zero : retirer les monstres, remettre le hero à fond en pv, mettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):
        #appliquer image du joueur
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        #appliquer ensemble images projectiles
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)

     #gestion mouvement joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x  + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
