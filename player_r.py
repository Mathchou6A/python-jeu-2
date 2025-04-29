import pygame

# créer une classe pour les deux joueur 

class PlayerR(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen
      
      # charger l'image du joueur
      self.image_passive = pygame.image.load('assets/player_r.png')
      self.rect = self.image_passive.get_rect()
      self.image_passive = pygame.transform.scale(self.image_passive, (129, 400))
      
      # charger l'image du joueur en mode atk
      self.image_atk = pygame.image.load('assets/player_r_atk.png')
      self.rect = self.image_atk.get_rect()
      self.image_atk = pygame.transform.scale(self.image_atk, (264, 400))
      
      # charger l'image du joueur en mode défense
      self.image_def = pygame.image.load('assets/player_r_def.png')
      self.rect = self.image_def.get_rect()
      self.image_def = pygame.transform.scale(self.image_def, (264, 400))
      
      self.status = "passive" # définir le statut du joueur
      
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.attack = 10
      self.velocity = 5
      self.rect.x = 1000
      self.rect.y = 200

   def attack_l(self):
      # changer le statut du joueur en mode attaque
      self.status = "atk"
      # jouer le son d'attaque
      self.game.sound_manager.play('tir')