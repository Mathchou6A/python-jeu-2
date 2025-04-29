import pygame


class Shield(pygame.sprite.Sprite):
   def __init__(self, game, player_l):
      super().__init__()
      self.game = game
      self.player_l = player_l
      self.image = pygame.image.load('assets/shield.png')
      self.image = pygame.transform.scale(self.image, (50, 50))
      self.rect = self.image.get_rect(center=(player_l.rect.x + 140, player_l.rect.y + 90))

      self.velocity = 10
      self.retour = False

   def move(self):
      if not self.retour:
         # déplacer le bouclier
         self.move_right()
         if self.rect.colliderect(self.game.player_r.rect):
            print("Bouclier touché PlayerR")
            self.retour = True
            self.game.player_r.domage(self.player_l.attack)

      # collision avec player_r → phase retour
      elif self.retour:
         self.move_left()
         if self.player_l.rect.x + 227 >= self.rect.x:
            # collision retour avec player_l → supprimer
            print("Bouclier revenu au joueur")
            self.remove()
            self.game.player_l.has_shield = False

   def move_right(self):
      self.rect.x += self.velocity

   def move_left(self):
      self.rect.x -= self.velocity
   
   def remove(self):
      self.game.shield.remove(self)



