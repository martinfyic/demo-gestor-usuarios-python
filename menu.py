import helpers


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

        opcion = input('> ')
        helpers.limpiar_consola()

        if opcion == '1':
            print('listando clientes')
        elif opcion == '2':
            print('Buscando cliente')
        elif opcion == '3':
            print('Agregando cliente')
        elif opcion == '4':
            print('Modificar cliente')
        elif opcion == '5':
            print('Borrar cliente')
        elif opcion == '6':
            print('Buscando cliente')
            break
        else:
            print('Opcion no valida!')

        input('\nPresiona ENTER para continuar...')
