import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_consola()

        print('=======================')
        print(' Bienvenido al Gestor  ')
        print('=======================')
        print()
        print('[1] Listar los clientes')
        print('[2] Buscar un cliente')
        print('[3] Agregar un cliente')
        print('[4] Modificar un cliente')
        print('[5] Borrar un cliente')
        print('[6] Cerrar el Gestor')
        print()
        print('=======================')

        opcion: str = input('> ')
        helpers.limpiar_consola()

        if opcion == '1':
            if len(db.Clientes.lista) == 0:
                print('No hay clientes en la base de datos')
            else:
                for cliente in db.Clientes.lista:
                    print(cliente)

        elif opcion == '2':
            if len(db.Clientes.lista) == 0:
                print('No hay clientes en la base de datos')
            else:
                dni: str = helpers.leer_texto(
                    8, 8, 'Ingrese un DNI (ejemplo 43236541)')
                cliente: db.Cliente = db.Clientes.buscar_cliente(dni)
                print(cliente)

        elif opcion == '3':
            dni: str | None = None
            while True:
                dni: str = helpers.leer_texto(
                    8, 8, 'Ingrese un DNI (ejemplo 43236541)')
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre: str = helpers.leer_texto(
                3, 45, 'Ingrese un nombre').capitalize()
            apellido: str = helpers.leer_texto(
                3, 45, 'Ingrese un apellido').capitalize()
            print()
            print('Cliente agregado correctamente') if db.Clientes.crear_cliente(
                dni, nombre, apellido) else print('Cliente no agregado')

        elif opcion == '4':
            if len(db.Clientes.lista) == 0:
                print('No hay clientes en la base de datos')
            else:
                dni: str = helpers.leer_texto(
                    8, 8, 'Ingrese un DNI (ejemplo 43236541)')
                cliente: db.Cliente = db.Clientes.buscar_cliente(dni)
                if cliente:
                    nombre: str = helpers.leer_texto(
                        3, 45, f'Ingrese un nombre [{cliente.nombre}]').capitalize()
                    apellido: str = helpers.leer_texto(
                        3, 45, f'Ingrese un apellido [{cliente.apellido}]').capitalize()
                    db.Clientes.modificar_cliente(
                        dni, nombre, apellido)
                    print('Cliente modificado correctamente')
                else:
                    print(f'No se encontro el cliente con DNI: {dni}')

        elif opcion == '5':
            if len(db.Clientes.lista) == 0:
                print('No hay clientes en la base de datos')
            else:
                dni: str = helpers.leer_texto(
                    8, 8, 'Ingrese un DNI (ejemplo 43236541)')
                print()
                print('Cliente eliminado correctamente') if db.Clientes.borrar_cliente(
                    dni) else print('Cliente no encontrado')

        elif opcion == '6':
            break
        else:
            print('Opcion no valida!')

        input('\nPresiona ENTER para continuar...')
