import pygame
import random


class Bombe(pygame.sprite.Sprite):
   def __init__(self, game, player_r):
      super().__init__()
      self.game = game
      self.player_r = player_r
      self.image = pygame.image.load('assets/bombe.png')
      self.image = pygame.transform.scale(self.image, (50, 50))
      self.rect = self.image.get_rect()

      self.velocity = 3

      
      self.rect.x = self.game.player_l.rect.x + 105
      self.rect.y = 0
   
   # def move(self):
   #    if not self.player_r.has_bombe:
   #       self.move_bottom()
   #       if self.rect.colliderect(self.game.player_l.rect):
   #          print("Bouclier touché PlayerR")
   #          self.game.player_l.domage(self.player_r.attack)
   #          self.remove()
   #          self.player_r.has_bombe = True

   def move(self):

      self.rect.y += self.velocity
      if self.rect.colliderect(self.game.player_l.rect):
         print("Bombe touché PlayerL")
         if self.game.player_l.status == "def":
            print("PlayerL se défend !")
            self.remove()
         else:
            self.game.player_l.domage(self.player_r.attack) 
            self.remove()
      elif self.rect.y > self.game.screen.get_height():
         self.remove()


   
   def remove(self):
      self.game.bombe.remove(self)
      self.player_r.has_bombe = False
