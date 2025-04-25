import pygame

# créer une classe pour les deux joueur 

class PlayerL(pygame.sprite.Sprite):
   def __init__(self, game, name):
      super().__init__()
      self.game = game # récupérer le jeu
      self.image = pygame.image.load('assets/player_l.png')
      self.rect = self.image.get_rect()