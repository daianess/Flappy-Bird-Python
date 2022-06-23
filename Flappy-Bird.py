import pygame
import os
import random

telaLargura = 500
telaAltura = 800

imagemCano = pygame.transform.scale2x(
    pygame.image.load(os.path.join('img', 'pipe.png')))
imagemChao = pygame.transform.scale2x(
    pygame.image.load(os.path.join('img', 'base.png')))
imagemBackground = pygame.transform.scale2x(
    pygame.image.load(os.path.join('img', 'bg.png')))
imagensBird = [
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('img', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('img', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('img', 'bird3.png'))),
]

pygame.font.init()
fontePontos = pygame.font.SysFont('arial', 50)


class Passaro:
    imgs = imagensBird
    # animações da rotação
    rotacaoMaxima = 25
    velocidadeRotacao = 20
    tempoAnimacao = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0


class Cano:
    pass


class Chao:
    pass
