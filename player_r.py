import pygame
from bombe import Bombe

class PlayerR(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game
      self.screen = screen
      self.bombe = Bombe(self.game, self)
      self.image_passive = pygame.image.load('assets/player_r.png')
      self.image_passive = pygame.transform.scale(self.image_passive, (129, 400))
      self.rect = self.image_passive.get_rect()
      
      self.image_atk = pygame.image.load('assets/player_r_atk.png')
      self.image_atk = pygame.transform.scale(self.image_atk, (264, 400))
      self.rect = self.image_atk.get_rect()

      
      self.status = "passive"
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.attack = 75
      self.velocity = 3
      self.rect.x = 1000
      self.rect.y = 200
      
      self.has_bombe = False
   
   def domage(self, attack):
      # infliger des dégâts au joueur
      self.health -= attack
      if self.health <= 0:
         self.game.score += 100
         self.game.game_over()
   
   def atk_r(self):
      self.status = "atk"
      print("PlayerR attaque !")
      if not self.has_bombe:
         bombe = Bombe(self.game, self)
         self.game.bombe.add(bombe)
         self.has_bombe = True
      # self.status = "passive"
      

   def move_left(self):
      if not self.game.check_collision():
         self.status = "passive"
         self.rect.x -= self.velocity  # avancer vers la gauche


   def move_right(self):
      self.status = "passive"
      self.rect.x += self.velocity  # reculer vers la droite






































# def update_ai(self, player_l):
   #    distance = self.rect.x - player_l.rect.x
      
   #    # Gestion du cooldown (attente entre les actions)
   #    if self.ia_cooldown > 0:
   #       self.ia_cooldown -= 1
   #       return
      
   #    # Priorité des actions
   #    if abs(distance) > 300:
   #       self.avancer()
   #    elif self.rect.x < 580:
   #       self.reculer()
   #    elif player_l.status == "atk": #  and random.randint(0, 2) == 0
   #       self.defendre()
   #    else:
   #       self.attaque()
      
   #    # Appliquer l'action choisie
   #    # if self.mode == "avancer":
   #    #    self.avancer()
   #    # elif self.mode == "attaquer":
   #    #    self.attaque(player_l)
   #    # elif self.mode == "défendre":
   #    #    self.defendre()
   #    # elif self.mode == "reculer":
   #    #    self.reculer()
      
   #    # Fixer un cooldown pour la prochaine action
   #    self.ia_cooldown = random.randint(30, 90)