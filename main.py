#PETIT Paul
#date de création : 18/01/2022
#Code sur la programation du jeu PONG

import core
import pygame
from pygame import *
import class_arene
import class_joueur
import class_balle


def setup():
    #fenetre
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]
    core.title = 'PONG'
    core.memory('colorfilet', (255, 255, 255))
    core.memory('posfiletl', Vector2(400, 0))
    core.memory('posfileth', Vector2(400, 600))
    core.memory('largeurfilet', 5)
    #Joueur1
    core.memory('posHaut', Vector2(20, 450))
    core.memory('posBas', Vector2(20, 500))
    core.memory('largeur', 10)
    core.memory('color',(255, 0, 0))
    core.memory("direction", Vector2(0, 0))
    #Adversaire
    core.memory('posHaut2', Vector2(780, 450))
    core.memory('posBas2', Vector2(780, 500))
    core.memory('largeur2', 10)
    core.memory('color2', (255, 0, 0))
    core.memory("direction2", Vector2(0, 0))
    #Ballon
    core.memory('color', (255, 255, 255))
    core.memory('posBall', Vector2(200,200))
    core.memory('rayonBall', 10)




def run():
    core.cleanScreen()

    pygame.draw.line(core.screen, core.memory('color'), core.memory('posHaut'), core.memory('posBas'), core.memory('largeur')) #Affiche joueur
    pygame.draw.line(core.screen, core.memory('color2'), core.memory('posHaut2'), core.memory('posBas2'), core.memory('largeur2')) #Affiche adversaire
    pygame.draw.circle(core.screen, core.memory("color"), core.memory("posBall"), core.memory("rayonBall")) #Affiche Balle
    pygame.draw.line(core.screen, core.memory('colorfilet'), core.memory('posfiletl'), core.memory('posfileth'), core.memory('largeurfilet')) #Affiche Filet

#Controle Joueur
    if core.getKeyPressList('K_z') :
        core.memory("direction", Vector2(core.memory("direction").y, -2))
    if core.getKeyPressList('K_s'):
        core.memory("direction", Vector2(core.memory("direction").y, 2))

        














core.main(setup, run)








