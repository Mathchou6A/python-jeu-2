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
      self.player_l = PlayerL(self, screen)
      self.player_r = PlayerR(self, screen)
      self.shield = pygame.sprite.Group()  # pour contenir tous les boucliers lancés
      self.bombe = pygame.sprite.Group()  # pour contenir toutes les bombes lancées
      self.soldat = Soldat(self)

      self.score = 0 
      
      
      self.perssed = {} # dictionnaire pour stocker les touches pressées
      
      # # gérer le sond
      self.sound_manager = SoundManager()
      
      self.font = pygame.font.Font('assets/ChelaOne-Regular.ttf', 25) # définir la police
   
   
   
   def health_bar_player_l(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [19, 69, self.player_l.max_health + 2, 32])
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [20, 70, self.player_l.max_health, 30])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [20, 70, self.player_l.health, 30])
      
      # bar_x = 20 + (self.player_l.max_health - self.player_l.health)
      # pygame.draw.rect(surface, (111, 210, 46), [bar_x, 70, self.player_l.health, 20])

   
   def health_bar_player_r(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [(self.screen.get_width() // 2 + 60) - 1, 69, self.player_r.max_health + 2, 30])
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.screen.get_width() // 2 + 60, 70, self.player_r.max_health, 28])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.screen.get_width() // 2 + 60, 70, self.player_r.health, 28])
   

   
   def start(self):
      self.is_playing = True
   
   def game_over(self):
      self.var_game_over = True
      # self.is_playing = False # remettre le jeu en attente
      print("Game Over")
      
      # remettre la vie du joueur à son maximum
      self.player_l.health = self.player_l.max_health 
      self.player_r.health = self.player_r.max_health 
      
      # remettre le joueur à sa position initiale
      self.player_l.rect.x = 55 
      self.player_r.rect.x = 1000
      
      # remettre le joueur à son statut initial
      self.player_l.status = "passive" 
      self.player_r.status = "passive"
      
      self.shield.remove(self.shield) # supprimer tous les boucliers
      self.player_l.has_shield = False
      
      self.score = 0 # remettre le score à 0
      # jouer le son de game over
      self.sound_manager.play('game_over') # jouer le son de game over

      self.soldat.reset_position()


   
   def update(self, screen, play_button, play_button_rect):
      # si game_over est vrai, afficher le message de game over
      if self.var_game_over:
         screen.blit(play_button, play_button_rect) # afficher le bouton
         if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(play_button_rect.collidepoint(event.pos)): # si le jeu n'a pas commencé
               self.is_playing = True
               self.var_game_over = False
         
         # afficher le message de game over
         if self.player_l.health <= 0:
            encouragement_text = self.font.render("Even if the fight is difficult, hold on!", 3, (255, 255, 255)) # définir le texte
            self.screen.blit(encouragement_text, (self.screen.get_width() // 2, self.screen.get_height() // 2)) # afficher le texte sur l'écran
            print("Player L a perdu !")
         elif self.player_r.health <= 0:
            encouragement_text = self.font.render("a changer par une meilleur phrase", 1, (255, 255, 255))
            self.screen.blit(encouragement_text, (200, 200))
            print("Player R a perdu !")
            
      if self.var_game_over == False:
         # print()
         # afficher le score sur l'écran
         score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0)) # définir le texte
         screen.blit(score_text, (20, 20)) # afficher le texte sur l'écran
         
         # Afficher le soldat (derrière PlayerR)
         self.soldat.move()
         screen.blit(self.soldat.image, self.soldat.rect)
         
         # appliquer l'image du joueur_l
         if self.player_l.status == "def":
            screen.blit(self.player_l.image_def, self.player_l.rect)
         else:
            if self.player_l.status == "passive":
               screen.blit(self.player_l.image_passive, self.player_l.rect)
            elif self.player_l.status == "atk": 
               screen.blit(self.player_l.image_atk, self.player_l.rect)

         # appliquer l'image du joueur_r
         if self.player_r.status == "passive":
            screen.blit(self.player_r.image_passive, self.player_r.rect)
         elif self.player_r.status == "atk": 
            screen.blit(self.player_r.image_atk, self.player_r.rect)
         
         
         # afficher et mettre à jour les boucliers
         for shield in self.shield:
            shield.move()
            screen.blit(shield.image, shield.rect)
         
         for bombe in self.bombe:
            bombe.move()
            screen.blit(bombe.image, bombe.rect)
         
         
         
         # afficher la barre de vie des joueurs
         self.health_bar_player_l(self.screen) 
         self.health_bar_player_r(self.screen)
         self.soldat.health_bar_soldat(self.screen)
         
         
         # verifier si le joueur soit aller à gauche ou à droite
         if self.perssed.get(pygame.K_d) and self.player_l.rect.x + 225 < screen.get_width(): # si la touche droite est enfoncée     
            self.player_l.move_right() # déplacer le joueur vers la droite   
         elif self.perssed.get(pygame.K_q) and self.player_l.rect.x > -10: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran    
            self.player_l.move_left() # déplacer le joueur vers la gauche

         if self.perssed.get(pygame.K_UP):
            self.player_r.atk_r()
         if self.perssed.get(pygame.K_LEFT):
            self.player_r.move_left()
         if self.perssed.get(pygame.K_RIGHT) and self.player_r.rect.x + 129< screen.get_width():
            self.player_r.move_right()


   
   def check_collision(self):
      if self.player_l.rect.x + 205 >= self.player_r.rect.x:
         return True
      else:
         return False
   
   def check_collision_soldat(self):
      if self.player_l.rect.x >= self.soldat.rect.x - 227:
         return True
      else:
         return False

