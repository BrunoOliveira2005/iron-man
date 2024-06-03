import pygame
import random

pygame.init()
tamanho = (800, 600)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("The Iron Man")

#CORES
branco = (255,255,255)
preto = (0,0,0)

#IMAGENS
iron = pygame.image.load("assets/iron.png")
missel = pygame.image.load("assets/missile.png")
fundo = pygame.image.load("assets/fundo.png")

#POSIÇÕES
posicaoXPersona = 400
posicaoYPersona = 300
movimentoXPersona = 0
movimentoYPersona = 0
posicaoXMissel = 400
posicaoYMissel = 0
velocidadeMissel = 1

#MUSICA
missileSound = pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.Sound.play(missileSound)
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)


#INICIO DO JOGO
while True:
    for evento in pygame.event.get():  ## Captura e devolve uma lista de eventos
        if evento.type == pygame.QUIT:
            quit()

        #X PERSONA
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona = 0

        #Y PERSONA
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona = 0

        #MISSEL
        if posicaoYMissel > 600:
            posicaoYMissel = -240
            posicaoXMissel == random.randint(0, 800)
            velocidadeMissel = velocidadeMissel + 2
            pygame.mixer.Sound.play(missileSound)
    
    posicaoXPersona = movimentoXPersona + posicaoXPersona
    posicaoYPersona = movimentoYPersona + posicaoYPersona
    posicaoYMissel = posicaoYMissel + velocidadeMissel

    ## TRAVA O MOVE  
    if posicaoXPersona < 0:
        posicaoXPersona = 0
    elif posicaoXPersona > 550:
        posicaoXPersona = 550
    if posicaoYPersona < 0:
        posicaoYPersona = 0
    elif posicaoYPersona > 463:
        posicaoYPersona = 463

    tela.blit(fundo, (0, 0))
    tela.blit(iron, (posicaoXPersona, posicaoYPersona))
    tela.blit(missel, (posicaoXMissel, posicaoYMissel - 200))

    # pygame.draw.circle(tela, preto, (posicaoXPersona, posicaoYPersona), 40, 40)
    # texto = fonte.render(str(posicaoXPersona) + "-" + str(posicaoYPersona), True, branco)
    # tela.blit(texto, (posicaoXPersona - 30, posicaoYPersona - 10))

    pygame.display.update()
    clock.tick(60)