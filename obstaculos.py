import pygame
import random
class Obstaculo:
    def __init__(self,arquivoImagem,Largura,altura,posY):
        self.imagem = pygame.image.load(arquivoImagem)
        self.largura = Largura
        self.altura = altura
        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.posX = random.randint(200,650)
        self.posY = posY
        self.vel = random.randint(3,5)
        self.mascara = pygame.mask.from_surface(self.imagem)

    def apareca(self,tela):
        tela.blit(self.imagem,(self.posX,self.posY))

    def movimentosSozinho (self):
        self.posY = self.posY + self.vel
        if self.posY >= 710:
            self.posY = 0
            self.vel = random.randint(3,5)
            self.posX = random.randint(200,650)
            