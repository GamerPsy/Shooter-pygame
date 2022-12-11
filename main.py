import pygame
pygame.init()

#generation de la fenêtre de jeu
pygame.display.set_caption("Mon shooter en python")
screen = pygame.display.set_mode((1080, 720))

#import de l'image de fond
background = pygame.image.load('assets/bg.jpg')



running = True

#Gameloop
while running:
    #appliquer l'arriere plan
    screen.blit(background,(0, -200))


    #mise à jour de l'écran
    pygame.display.flip()


    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
