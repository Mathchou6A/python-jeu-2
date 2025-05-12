import pygame
import random

# créer une classe pour les deux joueur 

class PlayerR(pygame.sprite.Sprite):
   def __init__(self, game, screen, player_l):
      super().__init__()
      self.game = game # récupérer le jeu
      self.screen = screen
      self.player_l = player_l
      
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

      self.ia_cooldown = 0  # pour gérer le rythme des actions
      self.mode = ""    # idle, avancer, attaquer, défendre, reculer

   def atk_l(self):
      # changer le statut du joueur en mode attaque
      self.status = "atk"
      # jouer le son d'attaque
      self.game.sound_manager.play('tir')
   
   def domage(self, attack):
      # infliger des dégâts au joueur
      self.health -= attack
      if self.health <= 0:
         self.game.game_over()
   
   def def_l(self):
      # changer le statut du joueur en mode défense
      self.status = "def"
      # jouer le son d'attaque
      # self.game.sound_manager.play('tir')
   
   def update_ai(self, distance):
      
      self.mode = random.choice(["avancer", "attaquer", "défendre", "reculer"])
      # if self.rect.x <= 580: 
      #    self.mode = "reculer"
      # if abs(distance) > 300:
      #    self.mode = "avancer"
      if self.player_l.status == "atk" and random.randint(0, 2) == 0:
         self.defandre()
      self.ia_cooldown = random.randint(30, 90)
      
      
      if self.mode == "avancer":
         self.avancer()
      if self.mode == "attaquer":
         self.attaque()
      if self.mode == "défendre":
         self.defandre()
      if self.mode == "reculer":
         self.reculer()
   
   def attaque(self):
      self.status = "atk"
   
   def avancer(self):
      self.status = "passive"
      self.rect.x -= self.velocity  # avancer vers la gauche
   
   def defandre(self):
      self.status = "def"
   
   def reculer(self):
      self.status = "passive"
      self.rect.x += self.velocity  # reculer vers la droite

      # if abs(distance) > 300:
      #    self.mode = "avancer"
      #    self.status = "passive"
      #    self.rect.x -= self.velocity  # avancer vers la gauche
      # elif abs(distance) < 200:
      #    self.mode = "passive"
      #    self.rect.x += self.velocity
      # else:
      #    self.mode = random.choice(["attaquer", "défendre", "reculer"])
      #    self.ia_cooldown = random.randint(30, 90)  # temps avant prochaine action (0.5 à 1.5s)
      #    if self.mode == "attaquer":
      #       self.status = "atk"
      #       self.game.sound_manager.play('tir')
      #       self.game.player_l.health -= self.attack
      #       if self.game.player_l.health <= 0:
      #          self.game.game_over()
      #    elif self.mode == "défendre":
      #       self.status = "def"
      #    elif self.mode == "reculer":
      #       self.status = "passive"
      #       self.rect.x += self.velocity  # reculer vers la droite
         
         


