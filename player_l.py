import pygame

# créer une classe pour les deux joueur 

class PlayerL(pygame.sprite.Sprite):
   def __init__(self, game):
      super().__init__()
      self.game = game # récupérer le jeu
      self.image = pygame.image.load('assets/player_l.png')
      self.rect = self.image.get_rect()
      self.image = pygame.transform.scale(self.image, (225, 400))
      self.max_health = 100
      self.health = 100
      self.attack = 10
      self.velocity = 5
      self.rect.x = 55
      self.rect.y = 200