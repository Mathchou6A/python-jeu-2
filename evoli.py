import pygame


# créer une classe pour les deux joueur 

class evoli(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen # récupérer l'écran
      
      # charger l'image du joueur
      self.image_passive = pygame.image.load('assets/evoli.png')
      self.rect = self.image_passive.get_rect()
      self.image_passive = pygame.transform.scale(self.image_passive, (225, 300))
      
      # charger l'image du joueur en mode attaque
      self.image_atk = pygame.image.load('assets/evoli_atk.png')
      self.rect = self.image_atk.get_rect()
      self.image_atk = pygame.transform.scale(self.image_atk, (227, 300))
      
      # charger l'image du joueur en mode défense
      self.image_def = pygame.image.load('assets/evoli_def.png')
      self.rect = self.image_def.get_rect()
      self.image_def = pygame.transform.scale(self.image_def, (264, 300))
      
      self.status = "passive" # définir le statut du joueur
      
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.velocity = 5
      self.rect.x = 1000
      self.rect.y = 201
      self.attack = 10
      
      self.couldown = 150
      


      
   def atk_l(self):
      self.attack = 10 + (self.rect.x / 7) # augmenter l'attaque en fonction de la position du joueur
      if not self.has_shield:
         self.status = "atk" 
         shield = Shield(self.game, self) # créer un bouclier
         self.game.shield.add(shield) # ajouter le bouclier au groupe
         self.has_shield = True

   
   def def_l(self):
      # changer le statut du joueur en mode attaque
      self.status = "def"
      print("PlayerL se défend !")
      
      
      
   def move_right(self):
      # tester la collision avec evoli avant de bouger
         self.rect.x += self.velocity
   
   
   def move_left(self):
      if not self.game.check_collision():
         self.rect.x -= self.velocity
   
   def domage(self, attack):
      # infliger des dégâts au joueur
      print("PlayerL touché !")
      self.health -= attack # réduire la santé du joueur
      print(f"Player a subi {attack} dégâts. Santé restante : {self.health}") # afficher les dégâts subis par le joueur
      if self.health <= 0: # si la santé est inférieure ou égale à 0, le joueur est mort
         self.game.game_over() 
   
   def timeur(self):
      self.couldown += 1




