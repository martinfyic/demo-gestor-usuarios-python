import csv
from typing import List
import config


class Cliente:
    def __init__(self, dni: str, nombre: str, apellido: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.dni} - {self.nombre} {self.apellido}'


class Clientes:

    lista: List[Cliente] = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar_cliente(dni: str) -> Cliente:
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear_cliente(dni: str, nombre: str, apellido: str) -> Cliente:
        cliente: Cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar_cliente(dni: str, nombre: str, apellido: str) -> Cliente:
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar_cliente(dni: str) -> Cliente:
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente_eliminado = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente_eliminado

    @staticmethod
    def guardar() -> None:
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow(
                    (cliente.dni, cliente.nombre, cliente.apellido))
