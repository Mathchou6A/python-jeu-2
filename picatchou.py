import pygame
from electric_charge import electric_charge

class picatchou(pygame.sprite.Sprite):
   def __init__(self, game, screen):
      super().__init__()
      self.game = game
      self.screen = screen
            
      self.image_passive = pygame.image.load('assets/picatchou.png')
      self.image_passive = pygame.transform.scale(self.image_passive, (315, 300))
      self.rect = self.image_passive.get_rect()
      
      self.image_atk = pygame.image.load('assets/picatchou_atk.png')
      self.image_atk = pygame.transform.scale(self.image_atk, (345, 300))
      self.rect = self.image_atk.get_rect()
      
      self.image_def = pygame.image.load('assets/picatchou_def.png')
      self.image_def = pygame.transform.scale(self.image_def, (272, 300))
      self.rect = self.image_def.get_rect()

      
      self.status = "passive"
      self.max_health = self.screen.get_width() / 2 - 80
      self.health = self.screen.get_width() / 2 - 80
      self.attack = 75
      self.velocity = 3
      self.rect.x = 55
      self.rect.y = 300
      
      self.has_shield = False # pour savoir si le joueur a un bouclier
      
   
   def domage(self, attack):
      # infliger des dégâts au joueur
      self.health -= attack
      if self.health <= 0:
         self.game.score += 100
         self.game.game_over()
   

   
   def atk_r(self):
      print(self.couldown)
      self.status = "atk"
      print("PlayerR attaque !")
      if not self.has_bombe and self.couldown >= 150:
         bombe = Bombe(self.game, self)
         self.game.bombe.add(bombe)
         self.has_bombe = True
         self.couldown = 0
         
      

   def move_right(self):
      if not self.game.check_collision(): # si le joueur n'est pas à la limite gauche de l'écran
         self.status = "passive"
         self.rect.x += self.velocity  # avancer vers la gauche


   def move_left(self): # avancer vers la droite
      if self.rect.x < 1280 + self.rect.width: # si le joueur n'est pas à la limite droite de l'écran
         self.status = "passive"
         self.rect.x -= self.velocity






































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