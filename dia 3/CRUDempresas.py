import os
import tabulate
import time
from librerias.libaempresas import buscar_empresa,mostrar_menu,cargar_datos,grabar_datos

f = open('empresas.txt','r')
str_empresas = f.read()
f.close()

lista_empresas = cargar_datos(str_empresas)
ANCHO = 50
opcion = 0


while(opcion < 5):
    os.system("cls")
    mostrar_menu(ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("cls")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC : ")
        razonsocial = input("RAZÓN SOCIAL : ")
        dirección = input("DIRECCIÓN : ")
        dic_nueva_empresa = {
            'RUC':ruc,
            'RAZÓN SOCIAL':razonsocial,
            'DIRECCIÓN':dirección
        }
        lista_empresas.append(dic_nueva_empresa)
        print(" EMPRESA REGISTRADA CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        cabeceras = ["RUC","RAZÓN SOCIAL","DIRECCIÓN"]
        tabla = [empre.values() for empre in lista_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RUC DE LA EMPRESA:')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresas)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA")
        else:
            print(f' EMPRESA A ACTUALIZAR : {lista_empresas[posicion_busqueda].get("RAZÓN SOCIAL")}')
            nuevo_ruc = input("RUC : ")
            nueva_razonsocial = input("RAZÓN SOCIAL : ")
            nueva_direccion = input("DIRECCIÓN : ")
            dic_actualizar_empresa = {
                'RUC':nuevo_ruc,
                'RAZÓN SOCIAL':nueva_razonsocial,
                'DIRECCIÓN':nueva_direccion
            }
            lista_empresas[posicion_busqueda] = dic_actualizar_empresa
            print("EMPRESA ACTUALIZADA CON EXITO...")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZÓN SOCIAL DE LA EMPRESA :')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresas)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA")
        else:
            lista_empresas.pop(posicion_busqueda)
            print('EMPRESA ELIMINADA!!!')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        str_empresas = grabar_datos(lista_empresas)
        fsalida = open('empresas.txt','w')
        fsalida.write(str_empresas)
        fsalida.close()
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)
