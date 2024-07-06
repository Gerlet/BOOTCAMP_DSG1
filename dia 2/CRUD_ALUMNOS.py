import os
import tabulate
import time
lista_alumnos = [
    {
        'nombre' : 'Gerardo Grande',
        'email' : 'elcoleccionista28gc@gmail.com',
        'celular' : '983762478',
    }

]

ancho=50
opcion=0

while (opcion<5):
    os.system("cls")
    print("="*ancho)
    print(" "*10 + "CRUD DE ALUMNOS")
    print("="*ancho)
    print("""

        [1] REGISTRAR ALUMNO
        [2] MOSTRAR ALUMNOS
        [3] ACTUALIZAR ALUMNO
        [4] ELIMINAR ALUMNO
        [5] SALIR  
          
          """)
    print("="*ancho)
    opcion=int(input("INGRESE OPCIÓN: "))
    os.system("cls")
    if(opcion==1):
        print("="*ancho)
        print(" "* 10 + "[1] REGISTRAR ALUMNO")
        print("="*ancho)
        nombre=input("NOMBRE : ")
        email=input("email: ")
        celular=input("celular : ")
        dic_nuevo_alumno = {

            'nombre' : nombre,
            'email' : email,
            'celular' : celular,
        }
        lista_alumnos.append(dic_nuevo_alumno)
        print("ALUMNO REGISTRADO CON EXITO :D ")
    elif(opcion==2):
        print("="*ancho)
        print(" "* 10 + "[2] MOSTRAR ALUMNO")
        print("="*ancho)
        cabeceras=["NOMBRE","EMAIL","CELULAR"]
        tabla=[alumno.values() for alumno in lista_alumnos]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        print(tabla)
    elif(opcion==3):
        print("="*ancho)
        print(" "* 10 + "[3] ACTUALIZAR ALUMNO")
        print("="*ancho)
        valor_busqueda=input('INGRESE EMAIL DEL ALUMNO A ACTUALIZAR :')
        posicion_busqueda=-1
        for posicion in range(len(lista_alumnos)):
            dic_alumno=lista_alumnos[posicion]
            if valor_busqueda in dic_alumno.values():
               posicion_busqueda=posicion
               break
        if posicion_busqueda==-1:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            print(f"ALUMNO A ACTUALIZAR : {lista_alumnos[posicion_busqueda].get("nombre")}")
            nuevo_nombre=input("NOMBRE : ")
            nuevo_email=input("EMAIL : ")
            nuevo_celular=input("CELULAR : ")
            dic_actualizar_alumno={
                'nombre' : nuevo_nombre,
                'email' : nuevo_email,
                'celular' : nuevo_celular,
            }

            lista_alumnos[posicion_busqueda]=dic_actualizar_alumno
            print("ALUMNO ACTUALIZADO CON EXITO :D ")
    elif(opcion==4):
        print("="*ancho)
        print(" "* 10 + "[4] ELIMINAR ALUMNO")
        print("="*ancho)
        valor_busqueda=input('INGRESE EMAIL DEL ALUMNO A ACTUALIZAR :')
        posicion_busqueda=-1
        for posicion in range(len(lista_alumnos)):
            dic_alumno=lista_alumnos[posicion]
            if valor_busqueda in dic_alumno.values():
               posicion_busqueda=posicion
               break
        if posicion_busqueda==-1:
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            lista_alumnos.pop(posicion_busqueda)
            print("ALUMNO ELIMINADO")
    elif(opcion==5):
        print("="*ancho)
        print(" "* 10 + "[5] SALIR")
        print("="*ancho)
    else:
        print("="*ancho)
        print(" "* 10 +"OPCIÓN INVALIDA!!!!")
        print("="*ancho)
        
    time.sleep(3)