# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.


from contabilidad import Contabilidad

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Netbeans')
    
mi_contabilidad = Contabilidad(2000, 40)

print(mi_contabilidad.obtener_sueldo())  
print(mi_contabilidad.obtener_horas())   


    