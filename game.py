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

      #appliquer l'image du joueur
      screen.blit(self.player_r.image, self.player_r.rect) 
      screen.blit(self.player_l.image, self.player_l.rect)
