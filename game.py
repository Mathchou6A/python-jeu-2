import pygame
from sounds import SoundManager # importer notre gestionnaire de son


class Game:
   def __init__(self):
      self.is_playing = False
      
      self.score = 0 
      
      self.perssed = {} # dictionnaire pour stocker les touches pressées
      
      # gérer le sond
      self.sound_manager = SoundManager()
      
      # self.font = pygame.font.Font('assets/ChelaOne-Regular.ttf', 25) # définir la police
   
   def start(self):
      self.is_playing = True
