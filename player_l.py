import pygame
from bouclier import Bouclier # type: ignore # importer le bouclier


# créer une classe pour les deux joueur 

class PlayerL(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen # récupérer l'écran
      # self.bouclier = Bouclier(self.game, self) # créer le bouclier du joueur gauche

      
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
      self.attack = 10
      self.velocity = 5
      self.rect.x = 55
      self.rect.y = 201
   
   def atk_l(self):
      # changer le statut du joueur en mode attaque
      self.status = "atk"
      # jouer le son d'attaque
      self.screen.blit(self.game.bouclier.image, self.game.bouclier.rect) # afficher le bouclier
      self.game.bouclier.move() # déplacer le bouclier
   
   def def_l(self):
      # changer le statut du joueur en mode attaque
      self.status = "def"
      # jouer le son d'attaque
      # self.game.sound_manager.play('tir')
      
      
   def move_right(self):
      # tester la collision avec player_r avant de bouger
      if not self.game.check_collision():
         self.rect.x += self.velocity
   
   
   def move_left(self):
      # if not self.game.check_collision():
         self.rect.x -= self.velocity





