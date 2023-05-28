import re
import os
import platform
from typing import List
from database import Cliente


def limpiar_consola():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')


def leer_texto(long_min: int = 0, long_max: int = 100, mensaje: str = None):
    print(mensaje) if mensaje else None
    while True:
        texto: str = input('> ')
        if long_min <= len(texto) <= long_max:
            return texto


def dni_valido(dni: str, lista: List[Cliente]):
    if not re.match('[0-9]{8}$', dni):
        print(f'DNI {dni} incorrecto!')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print(f'DNI {dni} ya existente')
            return False
    return True
