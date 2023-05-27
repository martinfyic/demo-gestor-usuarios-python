class Cliente:
    def __init__(self, dni: int, nombre: str, apellido: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.dni} - {self.nombre} {self.apellido}'


class Clientes:

    lista = []

    @staticmethod
    def buscar_cliente(dni: int) -> Cliente:
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear_cliente(dni: int, nombre: str, apellido: str) -> Cliente:
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente

    @staticmethod
    def modificar_cliente(dni: int, nombre: str, apellido: str) -> Cliente:
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                return Clientes.lista[indice]

    @staticmethod
    def borrar_cliente(dni: int) -> Cliente:
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                return Clientes.lista.pop(indice)
