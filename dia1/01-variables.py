#IMPUTS
print("Mi calculadora")
a=input("Ingrese un número por favor: ")
b=input("Ingrese otro número por favor: ")
operacion=input("Ingrese el tipo de operación por favor (suma|resta)")
#PRCESO
if(operacion=="suma"):
    resultado=int(a)+int(b)
else:
    resultado=int(a)-int(b)    
#OUTPUTS
print("El resultado es: ",resultado)