import pygame

# créer une classe pour les deux joueur 

class PlayerR(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen
      self.image = pygame.image.load('assets/player_r.png')
      self.rect = self.image.get_rect()
      self.image = pygame.transform.scale(self.image, (129, 400))
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.attack = 10
      self.velocity = 5
      self.rect.x = 1000
      self.rect.y = 200

