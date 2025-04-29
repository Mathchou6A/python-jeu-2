import pygame
import math
from game import Game # importer la classe game

pygame.init() # initialiser pygame

# def une clock 
clock = pygame.time.Clock() # créer une horloge pour le jeu
# définir le nombre de FPS
FPS = 60 # définir le nombre de FPS


# largeur de la fenêtre
largeur = 1280
# hauteur de la fenêtre
hauteur = 650

# créer une fenêtre de jeux
screen = pygame.display.set_mode((largeur, hauteur)) # définir la taille de la fenêtre   (1800, 950)
pygame.display.set_caption("Jeu pour l'anglais et la NSI")

background = pygame.image.load("assets/map_of_war.jpg") # charger l'arrière-plan

# charger notre bannière
banner = pygame.image.load("assets/banner.png") # charger la bannière
banner = pygame.transform.scale(banner, (500, 500)) # redimensionner la bannière
banner_rect = banner.get_rect() # récupérer le rectangle de la bannière
banner_rect.x = math.ceil(screen.get_width() // 2 - banner.get_width() // 2) # centrer la bannière

# charger notre bouton pour lancer le jeu
play_button = pygame.image.load("assets/button.png") # charger le bouton
play_button = pygame.transform.scale(play_button, (400, 150)) # redimensionner le bouton
play_button_rect = play_button.get_rect() # récupérer le rectangle du bouton
play_button_rect.x = math.ceil(screen.get_width() // 2 - play_button.get_width() // 2) # centrer le bouton
play_button_rect.y = math.ceil(screen.get_height() // 2 + play_button.get_height() // 2) # centrer le bouton


game = Game(screen) # charger notre jeu

# boucle de jeu
running = True

while running:
   # appliquer l'image de fond
   screen.blit(background, (0, -200)) 
   
   # verifier si le jeu a commencé
   if game.is_playing:
      game.update(screen) # declencher les instruction de la partie
   else:
      # afficher la bannière
      screen.blit(banner, banner_rect) # afficher la bannière
      screen.blit(play_button, play_button_rect) # afficher le bouton
      
      
      
   pygame.display.flip() # mettre à jour l'affichage
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")
      elif event.type == pygame.KEYDOWN: # si une touche est enfoncée
         game.perssed[event.key] = True
      
      # Déclenchement avec un clic gauche de souris
      elif event.type == pygame.MOUSEBUTTONDOWN:
         # vérifier si clic sur le bouton play
         if game.is_playing == False and play_button_rect.collidepoint(event.pos): # si le jeu n'a pas commencé
            game.start()
            print("Jeu commencé")
            # jouer le sond
            game.sound_manager.play('click') # jouer le son de clic
         else:
            if event.button == 1:
               game.player_l.atk_l()
               print("Attaque du joueur gauche")
            elif event.button == 3:
               game.player_l.def_l()
               print("Défense du joueur gauche")
      
      # elif event.type == pygame.MOU: 
      #    game.player_l.def_l()
      
      
      elif event.type == pygame.KEYUP: # si une touche est relâchée
         game.perssed[event.key] = False
         
   # limiter le nombre de FPS
   clock.tick(FPS) # limiter le nombre de FPS