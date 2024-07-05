import os
import tabulate
import time
lista_alumnos=[

    {
        'nombre':'Gerardo Grande',
        'email':'elcoleccionista28gc@gmail.com',
        'celular':'983762478'
    }
]

ancho=50
opc=0
while (opc<5):
    os.system("clear")
    print("="*ancho)
    print(""*10+"CRUD DE ALUMNOS")
    print("="*ancho)
    print("""
            [1] REGISTRAR ALUMNO
            [2] MOSTRAR ALUMNOS
            [3] ACTUALIZAR ALUMNO
            [4] ELIMINAR ALUMNO
            [5] SALIR
          """)
    
    print("="*ancho)
    opc=int(input("Ingrese una opción por favor: "))
    os.system("clear")
    print(f"Selecciona una opcion {opc}")
    time.sleep(3)