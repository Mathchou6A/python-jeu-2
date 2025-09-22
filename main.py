import pygame # importer pygame
import math # importer math
from game import Game # importer la classe game

pygame.init() # initialiser pygame

# def une clock 
clock = pygame.time.Clock() # créer une horloge pour le jeu
# définir le nombre de FPS
FPS = 60 # définir le nombre de FPS


# créer une fenêtre de jeux
screen = pygame.display.set_mode((1550, 800)) # définir la taille de la fenêtre   (1800, 950) (1280, 659)
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("street fighter pokemon") # définir le titre de la fenêtre

background = pygame.image.load("assets/map_pokemon.jpg") # charger l'arrière-plan
background = pygame.transform.scale(background, (1550, 800))

# charger notre bannière
banner = pygame.image.load("assets/banner_pokemon.png") # charger la bannière
banner = pygame.transform.scale(banner, (500, 200)) # redimensionner la bannière
banner_rect = banner.get_rect() # récupérer le rectangle de la bannière
banner_rect.x = math.ceil(screen.get_width() // 2 - banner.get_width() // 2) # centrer la bannière
banner_rect.y = math.ceil(screen.get_height() // 2 - 180) # centrer la bannière

# charger notre bouton pour lancer le jeu
play_button = pygame.image.load("assets/play_boutton.png") # charger le bouton
play_button = pygame.transform.scale(play_button, (225, 225)) # redimensionner le bouton
play_button_rect = play_button.get_rect() # récupérer le rectangle du bouton
play_button_rect.x = math.ceil(screen.get_width() // 2 - play_button.get_width() // 2) # centrer le 
play_button_rect.y = math.ceil(screen.get_height() // 2 + 100) # centrer le bouton


game = Game(screen) # charger notre jeu

# boucle de jeu
running = True

while running: # boucle principale du jeu
   # appliquer l'image de fond
   screen.blit(background, (0, 0)) 
   
   # verifier si le jeu a commencé
   if game.is_playing:
      game.update(screen, play_button, play_button_rect) # declencher les instruction de la partie
   else:
      # afficher la bannière
      screen.blit(banner, banner_rect) # afficher la bannière
      screen.blit(play_button, play_button_rect) # afficher le bouton
      
      # 
      # font = pygame.font.Font('assets/ChelaOne-Regular.ttf', 35) # définir la police
      # Encouragement_text_1 = font.render("I don't fight for a flag, but for what it represents:", 1, (255, 255, 255)) # définir le texte
      # Encouragement_text_2 = font.render("freedom, justice, and hope.", 1, (255, 255, 255))
      # Encouragement_text_3 = font.render("As long as there are men and women willing to stand up for these ideals, America will endure.", 1, (255, 255, 255))
      # Encouragement_text_4 = font.render("So let's rise together and show the world that these values will never fall.", 1, (255, 255, 255))
      
      # screen.blit(Encouragement_text_1, (screen.get_width() // 2 - Encouragement_text_1.get_width() // 2, 10)) # afficher le texte sur l'écran
      # screen.blit(Encouragement_text_2, (screen.get_width() // 2 - Encouragement_text_2.get_width() // 2, 45))
      # screen.blit(Encouragement_text_3, (screen.get_width() // 2 - Encouragement_text_3.get_width() // 2, 80))
      # screen.blit(Encouragement_text_4, (screen.get_width() // 2 - Encouragement_text_4.get_width() // 2, 115))
      
      
      
   pygame.display.flip() # mettre à jour l'affichage
   for event in pygame.event.get(): # boucle pour gérer les événements
      if event.type == pygame.QUIT: # si la croix de la fenêtre est cliquée
         running = False # quitter la boucle
         pygame.quit() # quitter le jeu
         print("Fermeture du jeu")
      elif event.type == pygame.KEYDOWN: # si une touche est enfoncée
         game.perssed[event.key] = True # enregistrer la touche enfoncée
      
      # Déclenchement avec un clic gauche de souris
      elif event.type == pygame.MOUSEBUTTONDOWN: # si un bouton de la souris est enfoncé
         
         # vérifier si clic sur le bouton play 
         if game.is_playing == False and play_button_rect.collidepoint(event.pos): # si le jeu n'a pas commencé
            game.start()
            print("Jeu commencé")
            # jouer le sond
            game.sound_manager.play('click') # jouer le son de clic
         elif game.var_game_over == True and play_button_rect.collidepoint(event.pos): # si le jeu est terminé
            game.start()
            print("Jeu commencé")
            # jouer le sond
            game.sound_manager.play('click') # jouer le son de clic
         else:
            if event.button == 1: # si le bouton gauche de la souris est enfoncé
               game.picatchou.atk_l() 
               print("Attaque du joueur gauche")
            elif event.button == 3: # si le bouton droit de la souris est enfoncé
               game.picatchou.def_l()
               print("Défense du joueur gauche")
      elif event.type == pygame.MOUSEBUTTONUP: # si un bouton de la souris est relâché
         if event.button == 3:
            game.picatchou.status = "passive"  # Désactiver la défense du joueur gauche
            # print("Fin de la défense du joueur gauche")
      
      
      
      elif event.type == pygame.KEYUP: # si une touche est relâchée
         game.perssed[event.key] = False
         
   # limiter le nombre de FPS
   clock.tick(FPS) 