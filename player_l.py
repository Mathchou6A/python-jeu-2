import pygame
from shield import Shield # type: ignore # importer le shield


# créer une classe pour les deux joueur 

class PlayerL(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen # récupérer l'écran
      # self.shield = shield(self.game, self) # créer le shield du joueur gauche

      
      # charger l'image du joueur
      self.image_passive = pygame.image.load('assets/player_l.png')
      self.rect = self.image_passive.get_rect()
      self.image_passive = pygame.transform.scale(self.image_passive, (225, 400))
      
      # charger l'image du joueur en mode attaque
      self.image_atk = pygame.image.load('assets/player_l_atk.png')
      self.rect = self.image_atk.get_rect()
      self.image_atk = pygame.transform.scale(self.image_atk, (227, 400))
      
      # charger l'image du joueur en mode défense
      self.image_def = pygame.image.load('assets/player_l_def.png')
      self.rect = self.image_def.get_rect()
      self.image_def = pygame.transform.scale(self.image_def, (264, 400))
      
      self.status = "passive" # définir le statut du joueur
      
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.velocity = 5
      self.rect.x = 55
      self.rect.y = 201
      self.attack = 10
      
      self.has_shield = False

      
   def atk_l(self):
      self.attack = 10 + (self.rect.x / 7)
      if not self.has_shield:
         self.status = "atk"
         shield = Shield(self.game, self)
         self.game.shield.add(shield)
         self.has_shield = True


   
   def def_l(self):
      # changer le statut du joueur en mode attaque
      self.status = "def"
      print("PlayerL se défend !")
      
      
      
   def move_right(self):
      # tester la collision avec player_r avant de bouger
      if not self.game.check_collision() and not self.game.check_collision_soldat():
         self.rect.x += self.velocity
   
   
   def move_left(self):
      # if not self.game.check_collision():
         self.rect.x -= self.velocity
   
   def domage(self, attack):
      # infliger des dégâts au joueur
      print("PlayerL touché !")
      print("dommage de", attack)
      self.health -= attack
      print(f"Player a subi {attack} dégâts. Santé restante : {self.health}")
      if self.health <= 0:
         self.game.game_over()





