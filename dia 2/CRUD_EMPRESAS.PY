import os
import tabulate
import time
lista_de_empresas = [
    {
        'RUC' : '20100128056',
        'RAZÓN SOCIAL' : 'SAGA FALABELLA S A',
        'DIRECCIÓN ' : 'Av. Paseo de la Republica Nro. 3220',
    }

]

ancho=50
opcion=0

while (opcion<5):
    os.system("cls")
    print("="*ancho)
    print(" "*10 + "CRUD DE EMPRESAS")
    print("="*ancho)
    print("""

        [1] REGISTRAR EMPRESA
        [2] MOSTRAR EMPRESAS
        [3] ACTUALIZAR EMPRESA
        [4] ELIMINAR EMPRESA
        [5] SALIR  
          
          """)
    print("="*ancho)
    opcion=int(input("INGRESE OPCIÓN: "))
    os.system("cls")
    if(opcion==1):
        print("="*ancho)
        print(" "* 10 + "[1] REGISTRAR EMPRESA")
        print("="*ancho)
        ruc=input("RUC : ")
        razon_social=input("RAZÓN SOCIAL : ")
        direccion=input("DIRECCIÓN : ")
        dic_nuevo_empresas = {

            'RUC' : ruc,
            'RAZÓN SOCIAL' : razon_social,
            'DIRECCIÓN' : direccion,
        }
        lista_de_empresas.append(dic_nuevo_empresas)
        print("EMPRESA REGISTRADA CON EXITO :D ")
    elif(opcion==2):
        print("="*ancho)
        print(" "* 10 + "[2] MOSTRAR EMPRESAS")
        print("="*ancho)
        cabeceras=["RUC","RAZÓN SOCIAL","DIRECCIÓN"]
        tabla=[empresa.values() for empresa in lista_de_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        print(tabla)
    elif(opcion==3):
        print("="*ancho)
        print(" "* 10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ancho)
        valor_busqueda=input('INGRESE RAZÓN SOCIAL DE LA EMPRESA :')
        posicion_busqueda=-1
        for posicion in range(len(lista_de_empresas)):
            dic_empresa=lista_de_empresas[posicion]
            if valor_busqueda in dic_empresa.values():
               posicion_busqueda=posicion
               break
        if posicion_busqueda==-1:
            print("NO SE ENCONTRO LA EMPRESA")
        else:
            print(f"EMPRESA A CAMBIAR : {lista_de_empresas[posicion_busqueda].get("RAZÓN SOCIAL")}")
            nuevo_ruc=input("RUC : ")
            nueva_razon_social=input("RAZÓN SOCIAL : ")
            nueva_direccion=input("DIRECCIÓN : ")
            dic_actualizar_empresa={
                'nombre' : nuevo_ruc,
                'email' : nueva_razon_social,
                'celular' : nueva_direccion,
            }

            lista_de_empresas[posicion_busqueda]=dic_actualizar_empresa
            print("EMPRESA ACTUALIZADA CON EXITO :D ")
    elif(opcion==4):
        print("="*ancho)
        print(" "* 10 + "[4] ELIMINAR EMPRESA")
        print("="*ancho)
        valor_busqueda=input('INGRESE EMAIL DE LA EMPRESA A ACTUALIZAR :')
        posicion_busqueda=-1
        for posicion in range(len(lista_de_empresas)):
            dic_empresa=lista_de_empresas[posicion]
            if valor_busqueda in dic_empresa.values():
               posicion_busqueda=posicion
               break
        if posicion_busqueda==-1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
        else:
            lista_de_empresas.pop(posicion_busqueda)
            print("EMPRESA ELIMINADA")
    elif(opcion==5):
        print("="*ancho)
        print(" "* 10 + "[5] SALIR")
        print("="*ancho)
    else:
        print("="*ancho)
        print(" "* 10 +"OPCIÓN INVALIDA!!!!")
        print("="*ancho)
        
    time.sleep(3)