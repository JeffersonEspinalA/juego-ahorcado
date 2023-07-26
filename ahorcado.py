import pygame
import random

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = 	(255, 0, 0)

# Función para elegir una palabra aleatoria
def elegir_palabra():
    with open("palabras.txt", "r", encoding="utf-8") as archivo:
        PALABRAS = [linea.strip() for linea in archivo]
    return random.choice(PALABRAS)

# Función para mostrar el mensaje en la pantalla
def mostrar_mensaje(mensaje, pantalla, tam_fuente, x, y):
    fuente = pygame.font.Font("font/Pangolin-Regular.ttf", tam_fuente)
    texto = fuente.render(mensaje, True, NEGRO)
    pantalla.blit(texto, (x, y))

# Función del juego
def juego_ahorcado():
    pygame.init()

    # Configuración de la pantalla
    ANCHO_PANTALLA = 450
    ALTO_PANTALLA = 600
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption('Ahorcado')
    icono = pygame.image.load("img/icono.png")
    pygame.display.set_icon(icono)
    fondo = pygame.image.load("img/hoja_cuadriculada.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))

    # Variables del juego
    palabra = elegir_palabra()
    palabra_adivinada = '_' * len(palabra)
    intentos = 5
    letras_intentadas = []
    game_over = False

    # Imágenes del ahorcado
    ahorcados = []
    ahorcados_rect = []
    for i in range(6):
        ahorcado = pygame.image.load(f"img/ahorcado_{i}.png")
        ahorcado = pygame.transform.scale(ahorcado, (250, 250))
        ahorcado.set_colorkey(BLANCO)
        ahorcado_rect = ahorcado.get_rect()
        ahorcado_rect.x = ANCHO_PANTALLA // 2 - (ahorcado_rect.width // 2)
        ahorcado_rect.y = 25
        ahorcados.append(ahorcado)
        ahorcados_rect.append(ahorcado_rect)

    # Letras que se mostrarán en la pantalla
    abecedario1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    fila1 = "     ".join(abecedario1)
    abecedario2 = ['H', 'I', 'J', 'K', 'L', 'M', 'N']
    fila2 = "     ".join(abecedario2)
    abecedario3 = ['Ñ', 'O', 'P', 'Q', 'R', 'S', 'T']
    fila3 = "     ".join(abecedario3)
    abecedario4 = ['U', 'V', 'W', 'X', 'Y', 'Z']
    fila4 = "     ".join(abecedario4)

    # Variables del circulo
    x_circulo = 70
    y_circulo = ALTO_PANTALLA // 2 + 80
    radio = 20
    contorno_circulo = 2

    # Variables del X
    tamanio_x = 20
    x_x = 70
    y_x = ALTO_PANTALLA // 2 + 80

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and game_over == False:
                letra = pygame.key.name(event.key).upper()
                if letra.isalpha() and len(letra) == 1:
                    if letra not in letras_intentadas:
                        letras_intentadas.append(letra)
                        if letra in palabra:
                            indices = [i for i, x in enumerate(palabra) if x == letra]
                            palabra_adivinada = list(palabra_adivinada)
                            for idx in indices:
                                palabra_adivinada[idx] = letra
                            palabra_adivinada = "".join(palabra_adivinada)
                        else:
                            intentos -= 1

        pantalla.fill(BLANCO)
        
        # Mostrar fondo
        pantalla.blit(fondo, (0,0))

        # Mostrar intentos restantes
        mostrar_mensaje("INTENTOS: " + str(intentos), pantalla, 25, 5, 5)

        # Mostrar gráfico del ahorcado
        pantalla.blit(ahorcados[intentos], ahorcados_rect[intentos])

        # Mostrar palabra a adivinar
        mostrar_mensaje("PALABRA: " + palabra_adivinada, pantalla, 30, 20, ALTO_PANTALLA // 2)

        # Mostrar las letras
        if game_over == False:
            mostrar_mensaje(fila1, pantalla, 30, 60, ALTO_PANTALLA // 2 + 60)
            mostrar_mensaje(fila2, pantalla, 30, 60, ALTO_PANTALLA // 2 + 120)
            mostrar_mensaje(fila3, pantalla, 30, 60, ALTO_PANTALLA // 2 + 180)
            mostrar_mensaje(fila4, pantalla, 30, 90, ALTO_PANTALLA // 2 + 240)

            for l in letras_intentadas:
                if l in abecedario1:
                    if l in palabra:
                        if l == 'A':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo, y_circulo), radio, contorno_circulo)
                        elif l == 'B':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 53, y_circulo), radio, contorno_circulo)
                        elif l == 'C':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (53 * 2), y_circulo), radio, contorno_circulo)
                        elif l == 'D':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (53 * 3), y_circulo), radio, contorno_circulo)
                        elif l == 'E':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (53 * 4), y_circulo), radio, contorno_circulo)
                        elif l == 'F':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (53 * 5), y_circulo), radio, contorno_circulo)
                        elif l == 'G':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (53 * 6), y_circulo), radio, contorno_circulo)
                    else:
                        if l == 'A':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x, y_x - tamanio_x), (x_x + tamanio_x, y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x, y_x + tamanio_x), (x_x + tamanio_x, y_x - tamanio_x), 5)
                        elif l == 'B':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 54, y_x - tamanio_x), (x_x + tamanio_x + 54, y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 54, y_x + tamanio_x), (x_x + tamanio_x + 54, y_x - tamanio_x), 5)
                        elif l == 'C':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 2), y_x - tamanio_x), (x_x + tamanio_x + (54 * 2), y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 2), y_x + tamanio_x), (x_x + tamanio_x + (54 * 2), y_x - tamanio_x), 5)
                        elif l == 'D':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 3), y_x - tamanio_x), (x_x + tamanio_x + (54 * 3), y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 3), y_x + tamanio_x), (x_x + tamanio_x + (54 * 3), y_x - tamanio_x), 5)
                        elif l == 'E':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 4), y_x - tamanio_x), (x_x + tamanio_x + (54 * 4), y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 4), y_x + tamanio_x), (x_x + tamanio_x + (54 * 4), y_x - tamanio_x), 5)
                        elif l == 'F':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 5), y_x - tamanio_x), (x_x + tamanio_x + (54 * 5), y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 5), y_x + tamanio_x), (x_x + tamanio_x + (54 * 5), y_x - tamanio_x), 5)
                        elif l == 'G':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 6), y_x - tamanio_x), (x_x + tamanio_x + (54 * 6), y_x + tamanio_x), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 6), y_x + tamanio_x), (x_x + tamanio_x + (54 * 6), y_x - tamanio_x), 5)
                elif l in abecedario2:
                    if l in palabra:
                        if l == 'H':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo, y_circulo + 60), radio, contorno_circulo)
                        elif l == 'I':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 48, y_circulo + 60), radio, contorno_circulo)
                        elif l == 'J':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (48 * 2), y_circulo + 60), radio, contorno_circulo)
                        elif l == 'K':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (48 * 3), y_circulo + 60), radio, contorno_circulo)
                        elif l == 'L':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (50 * 4), y_circulo + 60), radio, contorno_circulo)
                        elif l == 'M':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (50 * 5), y_circulo + 60), radio, contorno_circulo)
                        elif l == 'N':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (51 * 6), y_circulo + 60), radio, contorno_circulo)
                    else:
                        if l == 'H':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x, y_x - tamanio_x + 58), (x_x + tamanio_x, y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x, y_x + tamanio_x + 58), (x_x + tamanio_x, y_x - tamanio_x + 58), 5)
                        elif l == 'I':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 50, y_x - tamanio_x + 58), (x_x + tamanio_x + 50, y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 50, y_x + tamanio_x + 58), (x_x + tamanio_x + 50, y_x - tamanio_x + 58), 5)
                        elif l == 'J':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 2), y_x - tamanio_x + 58), (x_x + tamanio_x + (50 * 2), y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 2), y_x + tamanio_x + 58), (x_x + tamanio_x + (50 * 2), y_x - tamanio_x + 58), 5)
                        elif l == 'K':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 3), y_x - tamanio_x + 58), (x_x + tamanio_x + (50 * 3), y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 3), y_x + tamanio_x + 58), (x_x + tamanio_x + (50 * 3), y_x - tamanio_x + 58), 5)
                        elif l == 'L':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 4), y_x - tamanio_x + 58), (x_x + tamanio_x + (50 * 4), y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 4), y_x + tamanio_x + 58), (x_x + tamanio_x + (50 * 4), y_x - tamanio_x + 58), 5)
                        elif l == 'M':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 5), y_x - tamanio_x + 58), (x_x + tamanio_x + (50 * 5), y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 5), y_x + tamanio_x + 58), (x_x + tamanio_x + (50 * 5), y_x - tamanio_x + 58), 5)
                        elif l == 'N':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 6), y_x - tamanio_x + 58), (x_x + tamanio_x + (50 * 6), y_x + tamanio_x + 58), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (50 * 6), y_x + tamanio_x + 58), (x_x + tamanio_x + (50 * 6), y_x - tamanio_x + 58), 5)
                elif l in abecedario3:
                    if l in palabra:
                        if l == 'Ñ':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo, y_circulo + (60 * 2)), radio, contorno_circulo)
                        elif l == 'O':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 54, y_circulo + (60 * 2)), radio, contorno_circulo)
                        elif l == 'P':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (54 * 2), y_circulo + (60 * 2)), radio, contorno_circulo)
                        elif l == 'Q':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (54 * 3), y_circulo + (60 * 2)), radio, contorno_circulo)
                        elif l == 'R':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (54 * 4), y_circulo + (60 * 2)), radio, contorno_circulo)
                        elif l == 'S':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (54 * 5), y_circulo + (60 * 2)), radio, contorno_circulo)
                        elif l == 'T':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + (53 * 6), y_circulo + (60 * 2)), radio, contorno_circulo)
                    else:
                        if l == 'Ñ':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x, y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x, y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x, y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x, y_x - tamanio_x + (58 * 2)), 5)
                        elif l == 'O':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 56, y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x + 56, y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 56, y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x + 56, y_x - tamanio_x + (58 * 2)), 5)
                        elif l == 'P':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (56 * 2), y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x + (56 * 2), y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (56 * 2), y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x + (56 * 2), y_x - tamanio_x + (58 * 2)), 5)
                        elif l == 'Q':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 3), y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 3), y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 3), y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 3), y_x - tamanio_x + (58 * 2)), 5)
                        elif l == 'R':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 4), y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 4), y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 4), y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 4), y_x - tamanio_x + (58 * 2)), 5)
                        elif l == 'S':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 5), y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 5), y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 5), y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 5), y_x - tamanio_x + (58 * 2)), 5)
                        elif l == 'T':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 6), y_x - tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 6), y_x + tamanio_x + (58 * 2)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + (54 * 6), y_x + tamanio_x + (58 * 2)), (x_x + tamanio_x + (54 * 6), y_x - tamanio_x + (58 * 2)), 5)
                elif l in abecedario4:
                    if l in palabra:
                        if l == 'U':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 30, y_circulo + (60 * 3)), radio, contorno_circulo)
                        elif l == 'V':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 85, y_circulo + (60 * 3)), radio, contorno_circulo)
                        elif l == 'W':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 140, y_circulo + (60 * 3)), radio, contorno_circulo)
                        elif l == 'X':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 195, y_circulo + (60 * 3)), radio, contorno_circulo)
                        elif l == 'Y':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 250, y_circulo + (60 * 3)), radio, contorno_circulo)
                        elif l == 'Z':
                            pygame.draw.circle(pantalla, AZUL, (x_circulo + 305, y_circulo + (60 * 3)), radio, contorno_circulo)
                    else:
                        if l == 'U':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 30, y_x - tamanio_x + (60 * 3)), (x_x + tamanio_x + 30, y_x + tamanio_x + (60 * 3)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 30, y_x + tamanio_x + (60 * 3)), (x_x + tamanio_x + 30, y_x - tamanio_x + (60 * 3)), 5)
                        elif l == 'V':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 85, y_x - tamanio_x + (60 * 3)), (x_x + tamanio_x + 85, y_x + tamanio_x + (60 * 3)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 85, y_x + tamanio_x + (60 * 3)), (x_x + tamanio_x + 85, y_x - tamanio_x + (60 * 3)), 5)
                        elif l == 'W':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 140, y_x - tamanio_x + (60 * 3)), (x_x + tamanio_x + 140, y_x + tamanio_x + (60 * 3)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 140, y_x + tamanio_x + (60 * 3)), (x_x + tamanio_x + 140, y_x - tamanio_x + (60 * 3)), 5)
                        elif l == 'X':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 195, y_x - tamanio_x + (60 * 3)), (x_x + tamanio_x + 195, y_x + tamanio_x + (60 * 3)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 195, y_x + tamanio_x + (60 * 3)), (x_x + tamanio_x + 195, y_x - tamanio_x + (60 * 3)), 5)
                        elif l == 'Y':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 250, y_x - tamanio_x + (60 * 3)), (x_x + tamanio_x + 250, y_x + tamanio_x + (60 * 3)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 250, y_x + tamanio_x + (60 * 3)), (x_x + tamanio_x + 250, y_x - tamanio_x + (60 * 3)), 5)
                        elif l == 'Z':
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 305, y_x - tamanio_x + (60 * 3)), (x_x + tamanio_x + 305, y_x + tamanio_x + (60 * 3)), 5)
                            pygame.draw.line(pantalla, ROJO, (x_x - tamanio_x + 305, y_x + tamanio_x + (60 * 3)), (x_x + tamanio_x + 305, y_x - tamanio_x + (60 * 3)), 5)

        # Verificar si ganó o perdió
        if palabra_adivinada == palabra:
            mostrar_mensaje("¡Has ganado!", pantalla, 80, 10, 400)
            mostrar_mensaje("Jefferson William Espinal Atencia (2023) ©", pantalla, 10, 130, 580)
            game_over = True
        elif intentos == 0:
            mostrar_mensaje("¡Has perdido!", pantalla, 80, 10, 400)
            mostrar_mensaje("La palabra era: " + palabra, pantalla, 30, 10, 500)
            mostrar_mensaje("Jefferson William Espinal Atencia (2023) ©", pantalla, 10, 130, 580)
            game_over = True

        pygame.display.update()
        pygame.display.flip()

juego_ahorcado()
