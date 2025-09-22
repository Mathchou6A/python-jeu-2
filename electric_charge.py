import pygame


class electric_charge(pygame.sprite.Sprite):
   def __init__(self, game, player_l):
      super().__init__()
      self.game = game # récupérer le jeu
      self.picatchou = picatchou  # récupérer le joueur gauche
      self.image = pygame.image.load('assets/electric_charge.png') # charger l'image du bouclier
      self.image = pygame.transform.scale(self.image, (100, 100)) # redimensionner l'image
      self.rect = self.image.get_rect(center=(player_l.rect.x + 140, player_l.rect.y + 90)) # positionner le bouclier au niveau du joueur

      self.velocity = 10 # vitesse de déplacement du bouclier
      self.retour = False # phase retour

   def move(self):
      # déplacer le bouclier
      self.move_right() # déplacer vers la droit
      
      if self.rect.colliderect(self.game.evoli.rect): # collision avec player_r
         print("electric charge touch evoli")
         self.game.evoli.domage(self.player_l.attack) # infliger des dégâts au joueur de droite
         self.remove(self)



   def move_right(self): # déplacer le bouclier vers la droite
      self.rect.x += self.velocity

   def move_left(self): # déplacer le bouclier vers la gauche
      self.rect.x -= self.velocity
   
   def remove(self): # supprimer le bouclier du jeu
      self.game.electric_charge.remove(self)



