import pygame
from sys import exit
from random import randint, choice
pygame.init()

def animacao_plataforma():
    # Calcula o movimento da plataforma
    plataforma_retangulo.x += movimento_plataforma

    if plataforma_retangulo.right > 700:
      plataforma_retangulo.right = 700
    elif plataforma_retangulo.left <= 0:
       plataforma_retangulo.left = 0

    tela.blit(plataforma, plataforma_retangulo)

def animacao_bola():
    # Calcula o movimento da plataforma
    bola_retangulo.x += movimento_bola

    if bola_retangulo.right > 700:
      bola_retangulo.right = 700
    elif bola_retangulo.left <= 0:
       bola_retangulo.left = 0

    tela.blit(bola, bola_retangulo)

def posicao_cristais():
    global lista_cristais

    cristais_lista_aleatoria = ['amarelo'] + ['azul'] + ['branco'] + ['laranja'] + ['preto'] + ['rosa'] + ['roxo'] + ['verde'] + ['verdeamarelado'] + ['vermelho'] 
    tipo_objeto = choice(cristais_lista_aleatoria)

    posicao = (randint(30,670), randint(30,240))

    if tipo_objeto == 'amarelo':
        objeto_rect = cristalamarelo_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'azul':
        objeto_rect = cristalazul_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'branco':
        objeto_rect = cristalbranco_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'laranja':
        objeto_rect = cristallaranja_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'preto':
        objeto_rect = cristalpreto_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'rosa':
        objeto_rect = cristalrosa_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'roxo':
        objeto_rect = cristalroxo_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'verde':
        objeto_rect = cristalverde_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'verdeamarelado':
        objeto_rect = cristalverdeamarelado_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'vermelho':
        objeto_rect = cristalvermelho_surfaces[0].get_rect(center = posicao)

    lista_cristais.append({
        'tipo': tipo_objeto,
        'retangulo': objeto_rect
    })

    tela.blit(posicao_cristais)

# Cria a tela
tamanho = (700, 540)
tela = pygame.display.set_mode(tamanho)

# Define o Titulo da Janela
pygame.display.set_caption("Crystal Breaker")

##
## Importa os arquivos necessários
##

# Carrega o plano de fundo -----------------------------
plano_fundo = pygame.image.load('background/background1.png').convert_alpha()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)

## Bola ------------------------------------------------
# Carrega as imagens da bola
bola = pygame.image.load('bola/bola1.png').convert_alpha()
bola = pygame.transform.scale(bola, (20, 20))

bola_retangulo = bola.get_rect(center = (350, 480))

## Plataforma -------------------------------------------
# Carrega as imagens da plataforma
plataforma = pygame.image.load('plataforma/plataforma1.png').convert_alpha()
plataforma = pygame.transform.scale(plataforma, (200, 30))

plataforma_retangulo = plataforma.get_rect(center = (350, 510))

### Cristais ---------------------------------------------
## Carrega as imagens da crystal

lista_cristais = []
# Crystal Amarelo
cristalamarelo_surfaces = []
cristalamarelo_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_amarelo/amarelo{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalamarelo_surfaces.append(img)

# Crystal Azul
cristalazul_surfaces = []
cristalazul_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_azul/azul{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalazul_surfaces.append(img)

# Crystal Branco
cristalbranco_surfaces = []
cristalbranco_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_branco/branco{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalbranco_surfaces.append(img)

# Crystal Laranja
cristallaranja_surfaces = []
cristallaranja_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_laranja/laranja{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristallaranja_surfaces.append(img)

# Crystal Preto
cristalpreto_surfaces = []
cristalpreto_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_preto/preto{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalpreto_surfaces.append(img)

# Crystal Rosa
cristalrosa_surfaces = []
cristalrosa_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_rosa/rosa{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalrosa_surfaces.append(img)

# Crystal Roxo
cristalroxo_surfaces = []
cristalroxo_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_roxo/roxo{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalroxo_surfaces.append(img)

# Crystal Verde
cristalverde_surfaces = []
cristalverde_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_verde/verde{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalverde_surfaces.append(img)

# Crystal Verde Amarelado
cristalverdeamarelado_surfaces = []
cristalverdeamarelado_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_verdeamarelado/verdeamarelado{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalverdeamarelado_surfaces.append(img)

# Crystal Vermelho
cristalvermelho_surfaces = []
cristalvermelho_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'cristais/cristais_vermelho/vermelho{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (50,50))
    cristalvermelho_surfaces.append(img)

# Cria um relógico para controlar os FPS
relogio = pygame.time.Clock()

# Controla se o personagem está andando (negativo esquerda, positivo direita)
movimento_plataforma = 0
direcao_plataforma = 0
movimento_bola = 0
vida = 3

#Loop principal do jogo
while True:
    ## EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                movimento_plataforma = 5
                direcao_plataforma = 1

            if evento.key == pygame.K_a:
                movimento_plataforma = -5
                direcao_plataforma = 0

            if evento.key == pygame.K_RIGHT:
                movimento_plataforma = 5
                direcao_plataforma = 1

            if evento.key == pygame.K_LEFT:
                movimento_plataforma = -5
                direcao_plataforma = 0

            if evento.key == pygame.K_UP:
                movimento_plataforma = 0

    # Desenha o fundo na tela
    tela.blit(plano_fundo, (0,0))

    animacao_plataforma()

    animacao_bola()

    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)