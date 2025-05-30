import pygame


class Shield(pygame.sprite.Sprite):
   def __init__(self, game, player_l):
      super().__init__()
      self.game = game # récupérer le jeu
      self.player_l = player_l # récupérer le joueur gauche
      self.image = pygame.image.load('assets/shield.png') # charger l'image du bouclier
      self.image = pygame.transform.scale(self.image, (100, 100)) # redimensionner l'image
      self.rect = self.image.get_rect(center=(player_l.rect.x + 140, player_l.rect.y + 90)) # positionner le bouclier au niveau du joueur

      self.velocity = 10 # vitesse de déplacement du bouclier
      self.retour = False # phase retour

   def move(self):
      if not self.retour:
         # déplacer le bouclier
         self.move_right() # déplacer vers la droite
         if self.rect.colliderect(self.game.player_r.rect): # collision avec player_r
            print("Bouclier touché PlayerR")
            self.retour = True
            self.game.player_r.domage(self.player_l.attack) # infliger des dégâts au joueur de droite
         elif self.rect.colliderect(self.game.soldat.rect): # collision avec soldat
            print("Bouclier touché Soldat")
            self.game.score += 5 # ajouter 5 points au score
            self.retour = True # phase retour
            self.game.soldat.domage(38) # infliger 38 de dégâts au soldat

      # collision avec player_r → phase retour
      elif self.retour: 
         self.move_left() # déplacer vers la gauche
         if self.player_l.rect.x + 227 >= self.rect.x:
            # collision retour avec player_l → supprimer
            print("Bouclier revenu au joueur")
            self.player_l.status = "passive"
            self.retour = False
            self.remove() # supprimer le bouclier
            self.game.player_l.has_shield = False

   def move_right(self): # déplacer le bouclier vers la droite
      self.rect.x += self.velocity

   def move_left(self): # déplacer le bouclier vers la gauche
      self.rect.x -= self.velocity
   
   def remove(self): # supprimer le bouclier du jeu
      self.game.shield.remove(self)



