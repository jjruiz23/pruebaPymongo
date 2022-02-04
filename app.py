# import insert
# import read
# import update
# import delete

def run():

    Bienvenida = '''BIENVENIDO
        1) INSERT
        2) UPDATE
        3) READ
        4) DELETE
        '''
    print(Bienvenida)

    menu()


def menu():

    verificador = True

    while verificador:
        mensaje = '''Seleccione una opcion : '''

        opc = int(input(mensaje))

        if opc == 1:
            print('INSERTANDO')
            verificador = False
            #insert.insert()
        elif opc == 2:
            print('ACTUALIZANDO')
            verificador = False
            #read.read()
        elif opc == 3:
            print('LEYENDO')
            verificador = False
            #update.update()
        elif opc == 4:
            print('ELIMINANDO')
            verificador = False
            #delete.delete()
        else:
            print('Opcion invalida \r\n')




if __name__ == '__main__':
    run()