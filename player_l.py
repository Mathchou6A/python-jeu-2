import pygame

# créer une classe pour les deux joueur 

class PlayerL(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen # récupérer l'écran
      self.image = pygame.image.load('assets/player_l.png')
      self.rect = self.image.get_rect()
      self.image = pygame.transform.scale(self.image, (225, 400))
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.attack = 10
      self.velocity = 5
      self.rect.x = 55
      self.rect.y = 201
   
   # def attack_l(self):
   #    # tester la collision avec player_r avant de bouger
   #    if self.game.check_collision():
         
   
   def move_right(self):
      # tester la collision avec player_r avant de bouger
      if not self.game.check_collision():
         self.rect.x += self.velocity
      
   
   def move_left(self):
      # if not self.game.check_collision():
         self.rect.x -= self.velocity





