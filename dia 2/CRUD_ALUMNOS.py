import tabulate
import os
import time

ancho=50
opc=0
while(opc<5):
    os.system("cls")
    print("="*ancho)
    print(" "*10 +"CRUD DE ALUMNOS")
    print("="*ancho)
    print("""

          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNOS
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO
          [5] SALIR
          """)
    print("="*ancho)
    opc=int(input("ingrese una opción por favor: "))
    os.system("cls")
    print(f"selecciono la opción {opc}")
    time.sleep(3)

