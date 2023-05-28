class Cliente:
    def __init__(self, dni: str, nombre: str, apellido: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.dni} - {self.nombre} {self.apellido}'


class Clientes:

    lista: list = []

    @staticmethod
    def buscar_cliente(dni: str) -> Cliente:
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear_cliente(dni: str, nombre: str, apellido: str) -> Cliente:
        cliente: Cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente

    @staticmethod
    def modificar_cliente(dni: str, nombre: str, apellido: str) -> Cliente:
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                return Clientes.lista[indice]

    @staticmethod
    def borrar_cliente(dni: str) -> Cliente:
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                return Clientes.lista.pop(indice)
