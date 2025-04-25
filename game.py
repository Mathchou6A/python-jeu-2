import pygame
from sounds import SoundManager # importer notre gestionnaire de son
from player_r import PlayerR # importer le joueur de droite
from player_l import PlayerL # importer le joueur de gauche


class Game:
   def __init__(self):
      self.is_playing = False
      self.player_r = PlayerR(self)
      self.player_l = PlayerL(self)
      self.score = 0 
      
      self.perssed = {} # dictionnaire pour stocker les touches pressées
      
      # # gérer le sond
      self.sound_manager = SoundManager()
      
      self.font = pygame.font.Font('assets/ChelaOne-Regular.ttf', 25) # définir la police
      
   
   def start(self):
      self.is_playing = True
   
   def update(self, screen):
      # afficher le score sur l'écran
      score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0)) # définir le texte
      screen.blit(score_text, (20, 20)) # afficher le texte sur l'écran
      
      # verifier si le joueur soit aller à gauche ou à droite
      if self.perssed.get(pygame.K_d) and self.player_l.rect.x + 225 < screen.get_width(): # si la touche droite est enfoncée      
         self.player_l.move_right() # déplacer le joueur vers la droite   
      elif self.perssed.get(pygame.K_q) and self.player_l.rect.x > -10: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran    
         self.player_l.move_left() # déplacer le joueur vers la gauche

      #appliquer l'image du joueur
      screen.blit(self.player_r.image, self.player_r.rect) 
      screen.blit(self.player_l.image, self.player_l.rect)
   
   # def check_collision(self, sprite, group):
   #    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # vérifier si le joueur touche un monstre
