import pygame
from pygame import *

class Ball :
    def __init__(self):
        self.rayon = 5
        self.couleur = (255, 255, 255)
        self.vitesse = Vector2()
        self.position = Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen,self.color, self.position, self.rayon)



