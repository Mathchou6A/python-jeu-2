import pygame
from sounds import SoundManager # importer notre gestionnaire de son
from player_r import PlayerR # importer le joueur de droite
from player_l import PlayerL # importer le joueur de gauche
from shield import Shield # type: ignore # importer le shield


class Game:
   def __init__(self, screen):
      self.screen = screen
      self.is_playing = False
      self.player_r = PlayerR(self, screen)
      self.player_l = PlayerL(self, screen)
      self.shield = pygame.sprite.Group()  # pour contenir tous les boucliers lancés

      self.score = 0 
      
      
      self.perssed = {} # dictionnaire pour stocker les touches pressées
      
      # # gérer le sond
      self.sound_manager = SoundManager()
      
      self.font = pygame.font.Font('assets/ChelaOne-Regular.ttf', 25) # définir la police
   
   
   
   def health_bar_player_l(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [19, 69, self.player_l.max_health + 2, 22])
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [20, 70, self.player_l.max_health, 20])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [20, 70, self.player_l.health, 20])
      
      # bar_x = 20 + (self.player_l.max_health - self.player_l.health)
      # pygame.draw.rect(surface, (111, 210, 46), [bar_x, 70, self.player_l.health, 20])

   
   def health_bar_player_r(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [(self.screen.get_width() // 2 + 60) - 1, 69, self.player_r.max_health + 2, 22])
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.screen.get_width() // 2 + 60, 70, self.player_r.max_health, 20])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.screen.get_width() // 2 + 60, 70, self.player_r.health, 20])
   
   def start(self):
      self.is_playing = True
   
   def update(self, screen):
      # print(self.screen.get_width() // 2 - 40) # afficher 
      # afficher le score sur l'écran
      score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0)) # définir le texte
      screen.blit(score_text, (20, 20)) # afficher le texte sur l'écran
      
      #appliquer l'image du joueur_l
      if self.player_l.status == "passive":
         screen.blit(self.player_l.image_passive, self.player_l.rect)
      elif self.player_l.status == "atk": 
         screen.blit(self.player_l.image_atk, self.player_l.rect)
      elif self.player_l.status == "def":
         screen.blit(self.player_l.image_def, self.player_l.rect)
      
      # appliquer l'image du joueur_r
      if self.player_r.status == "passive":
         screen.blit(self.player_r.image_passive, self.player_r.rect)
      elif self.player_r.status == "atk": 
         screen.blit(self.player_r.image_atk, self.player_r.rect)
      elif self.player_r.status == "def":
         screen.blit(self.player_r.image_def, self.player_r.rect)
      
      # afficher et mettre à jour les boucliers
      for shield in self.shield:
         shield.move()
         screen.blit(shield.image, shield.rect)
         # self.shield.all_shield.draw(screen) # dessiner tous les boucliers sur l'écran

      
      # afficher la barre de vie des joueurs
      self.health_bar_player_l(self.screen) 
      self.health_bar_player_r(self.screen)
      
      
      # verifier si le joueur soit aller à gauche ou à droite
      if self.perssed.get(pygame.K_d) and self.player_l.rect.x + 225 < screen.get_width(): # si la touche droite est enfoncée      
         self.player_l.move_right() # déplacer le joueur vers la droite   
      elif self.perssed.get(pygame.K_q) and self.player_l.rect.x > -10: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran    
         self.player_l.move_left() # déplacer le joueur vers la gauche



   
   def check_collision(self):
      # return pygame.sprite.collide_rect(self.player_l, self.player_r)
      if self.player_l.rect.x + 205 >= self.player_r.rect.x:
         return True
      else:
         return False


