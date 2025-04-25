import pygame

# créer une classe pour les deux joueur 

class PlayerR(pygame.sprite.Sprite):
   def __init__(self, game, name):
      super().__init__()
      self.game = game # récupérer le jeu
      self.image = pygame.image.load('assets/player_r.png')
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100
      self.attack = 10
      self.velocity = 5
      self.rect.x = 400
      self.rect.y = 400

