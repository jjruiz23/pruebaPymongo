# import insert
# import read
# import update
# import delete

def run():  # principal funtion

    Bienvenida = '''BIENVENIDO
        1) INSERT
        2) UPDATE
        3) READ
        4) DELETE
        '''
    print(Bienvenida)

    menu()  # llamar funcion


def menu(): # funcion 

    verificador = True  # controlador del while

    while verificador:
        mensaje = 'Seleccione una opcion : '

        opc = int(input(mensaje))   # captura de dato con mensaje

        #switch
        if opc == 1:
            print('INSERTANDO')
            verificador = False # terminar ciclo while
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

# entry point
if __name__ == '__main__':
    run()   # principal function