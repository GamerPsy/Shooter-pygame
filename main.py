import pygame
from game import Game

pygame.init()

#generation de la fenêtre de jeu
pygame.display.set_caption("Mon shooter en python")
screen = pygame.display.set_mode((1080, 720))

#import de l'image de fond
background = pygame.image.load('assets/bg.jpg')

#chargement du jeu
game = Game()

running = True

#Gameloop
while running:
    #appliquer l'arriere plan
    screen.blit(background,(0, -200))
    #appliquer image du joueur
    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
    #appliquer ensemble images projectiles
    game.player.all_projectiles.draw(screen)
    game.all_monsters.draw(screen)

    #gestion mouvement joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x  + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
                game.player.lauch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
