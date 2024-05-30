# Created on : 29 may 2024, 21:42:43
# Author     : USUARIO


# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.



class Jugadores:

    def __init__(self, x, c):
        self.nombre = x
        self.apellidos = c

    def establecer_nombre(self, x):
        self.nombre = x

    def establecer_apellido(self, c):
        self.apellidos = c

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellidos(self):
        return self.apellidos