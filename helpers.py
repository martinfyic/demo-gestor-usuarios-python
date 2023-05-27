import os
import platform


def limpiar_consola():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')


def leer_texto(long_min=0, long_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input('>')
        if long_min <= len(texto) <= long_max:
            return texto
