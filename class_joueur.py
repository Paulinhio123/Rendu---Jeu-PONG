import pygame
from pygame import *
import core

class Joueur :

    def __init__(self):
        self.posHaut = Vector2(10,450)
        self.posBas = Vector2(10,550)
        self.largeur = 30
        self.color = (255, 0, 0)
        self.name = str('Joueur_1')
        self.position = Vector2(0, 0)


    def draw(self, screen) :
        pygame.draw.line(screen, color, self.posHaut, self.posBas, self.largeur)

    def move(self):
        pass









