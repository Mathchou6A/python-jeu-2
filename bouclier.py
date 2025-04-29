import pygame



# definir la classe qui va gérer le bouclier de notre joueur
class Bouclier(pygame.sprite.Sprite):
   def __init__(self, game, player_l):
      super().__init__()
      self.player_l = player_l
      self.game = game
      self.image = pygame.image.load('assets/bouclier.png')
      self.image = pygame.transform.scale(self.image, (50, 50))
      self.velocity = 15 # vitesse du projectile
      self.rect = self.image.get_rect()
      self.rect.x = player_l.rect.x + 140
      self.rect.y = player_l.rect.y + 90

   
   def move(self):
      self.rect.x += self.velocity # deplacer le projectile vers la droite
