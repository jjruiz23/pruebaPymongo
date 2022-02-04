import insert
import read
import update
import delete

def run():
    persona1 = Programa()
    persona1.menu()

class Programa:
    def __init__(self):
        self.dato = 1
    def menu(self):

        mensaje = '''SELECCIONE UNA OPCION
        1) INSERT
        2) UPDATE
        3) READ
        4) DELETE'''

        while self.dato:

             opcion = int(input(mensaje))




if __name__ == '__main__':
    run()