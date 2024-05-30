# Created on : 29 may 2024, 21:34:58
# Author     : USUARIO


# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.



   class Contabilidad:

    def __init__(self, c, b):
        self.sueldo = c
        self.horas = b

    def establece_sueldo(self, c):
        self.sueldo = c

    def establecer_horas(self, b):
        self.horas = b

    def obtener_sueldo(self):
        return self.sueldo

    def obtener_horas(self):
        return self.horas
