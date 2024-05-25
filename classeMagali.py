import pygame

class Magali: 

    def __init__(self,arquivoImagem,Largura,altura,posX,posY):
        self.imagem = pygame.image.load(arquivoImagem) 
        self.largura = Largura
        self.altura = altura
        self.imagem =  pygame.transform.scale(self.imagem,(self.largura,self.altura))
        self.posX = posX
        self.posY = posY
        self.mascara = pygame.mask.from_surface(self.imagem)

    def apareca(self,tela):
        tela.blit(self.imagem,(self.posX,self.posY))
    
    def movimentosTeclas (self,direita,esquerda):
        keys = pygame.key.get_pressed()
        if keys [direita]:
            if self.posX < 800 - self.largura:
                self.posX = self.posX + 5
            elif keys [esquerda]:
                if self.posX > 0:
                    self.posX = self.posX - 5


    def poder_especial(self,tecla):
        keys = pygame.key.get_pressed()
        if keys [tecla]:
            self.posX = 0
            self.posY = 400