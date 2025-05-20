import pygame
import random

class Soldat(pygame.sprite.Sprite):
   def __init__(self, game):
      super().__init__()
      self.game = game
      self.image = pygame.image.load('assets/soldat.png')
      self.image = pygame.transform.scale(self.image, (200, 300))  # Réduire la taille pour qu'il passe derrière Hitler
      self.rect = self.image.get_rect()

      self.health = 150
      self.max_health = 150
      self.attack = 3
      self.velocity = random.randint(1, 3)
      
      self.rect.x = self.game.screen.get_width()  # Position initiale à droite de l'écran
      self.rect.y = 215  # Hauteur ajustée pour passer derrière Hitler

   def move(self):
      # Déplacer le soldat de gauche à droite
      if not self.game.check_collision_soldat():
         self.rect.x -= self.velocity
      else: 
         print("Soldat touché PlayerL")
         # Si le soldat touche le joueur gauche, il inflige des dégâts sauf si le joueur est en mode défense
         if self.game.player_l.status != "def":
            self.game.player_l.domage(self.attack)

   def health_bar_soldat(self, surface):
      # bordure noire
      pygame.draw.rect(surface, (0, 0, 0), [self.rect.x + 9, self.rect.y - 31, self.max_health + 2, 12])
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 30, self.max_health, 10])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 30, self.health, 10])
   
   
   def domage(self, attack):
      self.health -= attack
      if self.health <= 0:
         self.reset_position()  # Réinitialiser à gauche plutôt que de supprimer
   
   def reset_position(self):
      # Réinitialiser la position hors de l'écran à gauche
      self.rect.x = self.game.screen.get_width()
      self.health = self.max_health  # Réinitialiser la santé
