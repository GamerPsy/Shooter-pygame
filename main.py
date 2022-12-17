import pygame
import math
from game import Game

pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60

#generation de la fenêtre de jeu
pygame.display.set_caption("Mon shooter en python")
screen = pygame.display.set_mode((1080, 720))

#import de l'image de fond
background = pygame.image.load('assets/bg.jpg')

#importer la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

start_button = pygame.image.load('assets/button.png')
start_button = pygame.transform.scale(start_button, (400, 150))
start_button_rect = start_button.get_rect()
start_button_rect.x = math.ceil(screen.get_width() / 3.33)
start_button_rect.y = math.ceil(screen.get_height() / 2)

#chargement du jeu
game = Game()

running = True

#Gameloop
while running:
    #appliquer l'arriere plan
    screen.blit(background,(0, -200))
    
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(start_button,(start_button_rect.x, start_button_rect.y))
        screen.blit(banner,(banner_rect.x, 0))

    #mise à jour de l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.lauch_projectile()
                else:
                    game.start()
                    game.soundManager.play('click')
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                game.start()
                game.soundManager.play('click')

    #fixe le nb de FPS
    clock.tick(FPS)