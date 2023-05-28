import config
import csv
import copy
import helpers
import unittest
import database as db


class TestDataBase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('11111111', 'Martin', 'Ferreira'),
            db.Cliente('20983645', 'Fernanda', 'Perez'),
            db.Cliente('14239862', 'Ernesto', 'Hernandez'),
            db.Cliente('20983512', 'Marcela', 'Lazo'),
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar_cliente('11111111')
        cliente_inexistente = db.Clientes.buscar_cliente('99999')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        cliente_nuevo = db.Clientes.crear_cliente(
            '98765432', 'Marcelo', 'Padilla')
        self.assertEqual(len(db.Clientes.lista), 5)
        self.assertEqual(cliente_nuevo.dni, '98765432')
        self.assertEqual(cliente_nuevo.nombre, 'Marcelo')
        self.assertEqual(cliente_nuevo.apellido, 'Padilla')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar_cliente('20983645'))
        cliente_modificado = db.Clientes.modificar_cliente(
            '20983645', 'Ferni', 'Bueno')
        self.assertEqual(cliente_a_modificar.dni, '20983645')
        self.assertEqual(cliente_a_modificar.nombre, 'Fernanda')
        self.assertEqual(cliente_a_modificar.apellido, 'Perez')
        self.assertEqual(cliente_modificado.dni, '20983645')
        self.assertEqual(cliente_modificado.nombre, 'Ferni')
        self.assertEqual(cliente_modificado.apellido, 'Bueno')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar_cliente('14239862')
        cliente_buscado = db.Clientes.buscar_cliente('14239862')
        self.assertEqual(len(db.Clientes.lista), 3)
        self.assertEqual(cliente_borrado.dni, '14239862')
        self.assertIsNone(cliente_buscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('99999999', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('11111111', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('123', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23fds', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar_cliente('11111111')
        db.Clientes.borrar_cliente('20983645')
        db.Clientes.borrar_cliente('14239862')
        db.Clientes.modificar_cliente(
            '20983512', 'PruebaTest', 'TestEscritura')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '20983512')
        self.assertEqual(nombre, 'PruebaTest')
        self.assertEqual(apellido, 'TestEscritura')
