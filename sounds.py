import pygame

class SoundManager: # gestionnaire de sons
   def __init__(self):
      # initialiser le dictionnaire des sons
      self.sounds = {
         'click': pygame.mixer.Sound('assets/sounds/click.ogg'),
         'game_over': pygame.mixer.Sound('assets/sounds/game_over.ogg'),
         'meteorite': pygame.mixer.Sound('assets/sounds/meteorite.ogg'),
         'tir': pygame.mixer.Sound('assets/sounds/tir.ogg'),
      }
   
   def play(self, name): # jouer un son par son nom
      self.sounds[name].play() # jouer le son

