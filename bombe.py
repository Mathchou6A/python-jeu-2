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
   

   def move(self):
      self.rect.y += self.velocity # descendre la bombe
      # collision avec le joueur gauche
      if self.rect.colliderect(self.game.player_l.rect):
         print("Bombe touché PlayerL")
         if self.game.player_l.status == "def":
            print("PlayerL se défend !")
            self.remove() # supprimer la bombe
         else:
            self.game.player_l.domage(self.player_r.attack) # infliger des dégâts
            self.remove()
      elif self.rect.y > self.game.screen.get_height():
         self.remove()

   
   def remove(self): # supprimer la bombe du jeu
      self.game.bombe.remove(self)
      self.player_r.has_bombe = False
      self.status = "passive"
