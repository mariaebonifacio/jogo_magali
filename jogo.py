import pygame
from classeMagali import *
from obstaculos import *
pygame.init()

tela = pygame.display.set_mode((1000,500))
titulo = pygame.display.set_caption("Pega frutinhas")
FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO,(1000,500))

magali = Magali("imagens/magali.png",150,100,0,400)

fonte = pygame.font.SysFont("Arial Black",16)
fonte2 = pygame.font.SysFont("ArialBlacj",25)
pontuacao = 0

lista_bons = [Obstaculo("imagens/abacaxi.webp",90,60,0),
             Obstaculo("imagens/banana.png",90,60,0),
             Obstaculo("imagens/framboesa.png",90,60,0),
             Obstaculo("imagens/kiwi.png",90,60,0),
             Obstaculo("imagens/limao.png",90,60,0),
             Obstaculo("imagens/maca.png",90,60,0),
             Obstaculo("imagens/melancia.png",90,60,0)]

lista_ruins = [Obstaculo("imagens/aviao.png",90,60,0),
              Obstaculo("imagens/bomba.png",90,60,0),
              Obstaculo("imagens/bola.png",90,60,0)]

clock = pygame.time.Clock()
rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


    tela.blit(FUNDO,(0,0))
    magali.apareca(tela)
    magali.movimentosTeclas(pygame.K_RIGHT,pygame.K_LEFT)
    magali.poder_especial(pygame.K_SPACE)

    for fruta in lista_bons:
        fruta.apareca(tela)
        fruta.movimentosSozinho()

        if magali.mascara.overlap(fruta.mascara,(magali.posX - fruta.posX, magali.posY - fruta.posY)):
            pontuacao = pontuacao + 1
            fruta.posY = 0
            fruta.posX = random.randint(200,600)

        if pontuacao == 10:
            texto_vencedor = fonte2.render("Você ganhou!!",False,(255,255,255))
            tela.blit(texto_vencedor, (400,250))
            pygame.display.update()
            pygame.time.wait(2000)
            rodando = False

    for brinquedos in lista_ruins:
        brinquedos.apareca(tela)
        brinquedos.movimentosSozinho()

        if magali.mascara.overlap(brinquedos.mascara,(brinquedos.posX - magali.posX, brinquedos.posY - magali.posY)):
            texto_perdedor = fonte2.render("Você perdeu!",False,(255,255,255))
            tela.blit(texto_perdedor, (400,250))
            pygame.display.update()
            pygame.time.wait(2000)
            rodando = False


    texto_magali = fonte.render(f"Pontuação Magali: {pontuacao}",False,(0,0,0))
    tela.blit(texto_magali,(0,0))
    pygame.display.update()
    clock.tick(90)