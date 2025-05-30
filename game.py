import pygame
from sounds import SoundManager # importer notre gestionnaire de son
from player_r import PlayerR # importer le joueur de droite
from player_l import PlayerL # importer le joueur de gauche
from shield import Shield # type: ignore # importer le shield
from soldat import Soldat # type: ignore # importer le soldat


class Game:
   def __init__(self, screen):
      self.screen = screen
      self.is_playing = False
      self.var_game_over = False
      self.player_l = PlayerL(self, screen) # créer le joueur de gauche
      self.player_r = PlayerR(self, screen) # créer le joueur de droite
      self.shield = pygame.sprite.Group()  # pour contenir tous les boucliers lancés
      self.bombe = pygame.sprite.Group()  # pour contenir toutes les bombes lancées
      self.soldat = Soldat(self)

      self.score = 0 
      
      
      self.perssed = {} # dictionnaire pour stocker les touches pressées
      
      # # gérer le sond
      self.sound_manager = SoundManager()
      
      self.font = pygame.font.Font('assets/ChelaOne-Regular.ttf', 40) # définir la police

   
   
   def health_bar_player_l(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [19, 69, self.player_l.max_health + 2, 32]) # dessiner la bordure noire
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [20, 70, self.player_l.max_health, 30]) # dessiner l'arrière-plan de la barre de vie
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [20, 70, self.player_l.health, 30]) # dessiner la barre de vie
      

   
   def health_bar_player_r(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [(self.screen.get_width() // 2 + 60) - 1, 69, self.player_r.max_health + 2, 30])
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.screen.get_width() // 2 + 60, 70, self.player_r.max_health, 28])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.screen.get_width() // 2 + 60, 70, self.player_r.health, 28])
   

   
   def start(self):
      self.is_playing = True  
      self.var_game_over = False
      # remettre la vie du joueur à son maximum
      self.player_l.health = self.player_l.max_health # remettre la vie du joueur à son maximum
      self.player_r.health = self.player_r.max_health # remettre la vie du joueur à son maximum
      self.score = 0 # remettre le score à 0
   
   def game_over(self):
      self.var_game_over = True
      # self.is_playing = False # remettre le jeu en attente
      print("Game Over")
            
      # remettre le joueur à sa position initiale
      self.player_l.rect.x = 55 
      self.player_r.rect.x = 1000
      
      # remettre le joueur à son statut initial
      self.player_l.status = "passive" 
      self.player_r.status = "passive"
      
      self.shield.remove(self.shield) # supprimer tous les boucliers
      self.player_l.has_shield = False 
      
      # jouer le son de game over
      self.sound_manager.play('game_over') # jouer le son de game over

      self.soldat.reset_position() # réinitialiser la position du soldat
      self.bombe.remove() # supprimer toutes les bombes


   
   def update(self, screen, play_button, play_button_rect):
      # si game_over est vrai, afficher le message de game over
      if self.var_game_over:
         # afficher le message de game over
         score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0)) # définir le texte
         screen.blit(score_text, (20, 20)) # afficher le texte sur l'écran
         if self.player_l.health <= 0: # si le joueur gauche est mort
            # définir le texte d'encouragement
            encouragement_text_1 = self.font.render("I may fall, but as long as there is a spark of justice, I will rise again. ", True, (255, 255, 255)) # définir le texte
            encouragement_text_2 = self.font.render("Evil may win a battle, but it will never win the war. Together, we will triumph.", True, (255, 255, 255))
            # afficher le texte sur l'écran
            self.screen.blit(encouragement_text_1, (self.screen.get_width() // 2 - encouragement_text_1.get_width() // 2, self.screen.get_height() // 2 - 90)) # afficher le texte sur l'écran
            self.screen.blit(encouragement_text_2, (self.screen.get_width() // 2 - encouragement_text_2.get_width() // 2, self.screen.get_height() // 2 - 50)) #afficher le texte sur l'écran

         elif self.player_r.health <= 0: # si le joueur droit est mort
            # définir le texte
            encouragement_text = self.font.render("Even if the fight is difficult, hold on!", True, (255, 255, 255)) 
            # afficher le texte sur l'écran
            self.screen.blit(encouragement_text, (self.screen.get_width() // 2 - encouragement_text.get_width() // 2, self.screen.get_height() // 2 - 50)) # afficher le texte sur l'écran
            
         screen.blit(play_button, play_button_rect) # afficher le bouton

         
      else: 
         # print() # afficher le message de jeu en cours pour le débug
         # afficher le score sur l'écran
         score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0)) # définir le texte
         screen.blit(score_text, (20, 20)) # afficher le texte sur l'écran
         
         # Afficher le soldat (derrière PlayerR)
         self.soldat.move()
         screen.blit(self.soldat.image, self.soldat.rect)
         
         # appliquer l'image du joueur_l
         if self.player_l.status == "def": # si le joueur de gauche est en défense
            screen.blit(self.player_l.image_def, self.player_l.rect) # afficher l'image de défense du joueur de gauche
         else:
            if self.player_l.status == "passive": # si le joueur de gauche est en mode passif
               screen.blit(self.player_l.image_passive, self.player_l.rect) # afficher l'image passive du joueur de gauche
            elif self.player_l.status == "atk": # si le joueur de gauche est en attaque
               screen.blit(self.player_l.image_atk, self.player_l.rect) # afficher l'image d'attaque du joueur de gauche

         self.player_r.timeur() # pour faire un coldown de l'attaque du joueur droite
         
         
         # appliquer l'image du joueur_r
         if self.player_r.status == "passive":
            screen.blit(self.player_r.image_passive, self.player_r.rect)
         elif self.player_r.status == "atk": 
            screen.blit(self.player_r.image_atk, self.player_r.rect)
         if self.player_r.has_bombe == False:
            self.player_r.status = "passive"
         
         
         # afficher et mettre à jour les boucliers
         for shield in self.shield: # pour chaque bouclier dans le groupe de boucliers
            shield.move() # déplacer le bouclier
            screen.blit(shield.image, shield.rect) # afficher le bouclier sur l'écran
         
         # afficher et mettre à jour les bombes
         for bombe in self.bombe:
            bombe.move()
            screen.blit(bombe.image, bombe.rect)
         
         
         
         # afficher la barre de vie
         self.health_bar_player_l(self.screen) # dessiner la barre de vie du joueur de gauche 
         self.health_bar_player_r(self.screen)
         self.soldat.health_bar_soldat(self.screen)
         
         
         # verifier si le joueur soit aller à gauche ou à droite
         if self.perssed.get(pygame.K_d) and self.player_l.rect.x + 225 < screen.get_width(): # si la touche droite est enfoncée     
            self.player_l.move_right() # déplacer le joueur vers la droite   
         elif self.perssed.get(pygame.K_q) and self.player_l.rect.x > -10: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran    
            self.player_l.move_left() # déplacer le joueur vers la gauche

         # vérifier les entrées des touche pour le joueur de droite
         if self.perssed.get(pygame.K_UP): # si la touche haut est enfoncée
            self.player_r.atk_r() # attaquer le joueur de droite
         if self.perssed.get(pygame.K_LEFT):
            self.player_r.move_left()
         if self.perssed.get(pygame.K_RIGHT) and self.player_r.rect.x + 129< screen.get_width():
            self.player_r.move_right()


   # vérifier la collision entre les joueurs
   def check_collision(self):
      if self.player_l.rect.x + 205 >= self.player_r.rect.x: # si les coordoner du joueur de gauche sont collision avec les coordoner du joueur de droite
         return True
      else:
         return False
   
   # vérifier la collision entre le joueur de gauche et le soldat
   def check_collision_soldat(self):
      if self.player_l.rect.x >= self.soldat.rect.x - 227: # si le joueur de gauche est en collision avec le soldat
         return True
      else:
         return False

