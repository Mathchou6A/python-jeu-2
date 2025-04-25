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
   
   
   def move_right(self):
   # si le joueur n'est pas en colision avec un monstre
      # if not self.game.check_collision(self, self.game.all_monsters):
      self.rect.x += self.velocity
   
   def move_left(self):
      self.rect.x -= self.velocity