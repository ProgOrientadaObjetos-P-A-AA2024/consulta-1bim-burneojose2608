# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Netbeans')
    
from jugadores import Jugadores


jugador = Jugadores("Juan", "Pérez")
print(jugador.obtener_nombre())     
print(jugador.obtener_apellidos())   