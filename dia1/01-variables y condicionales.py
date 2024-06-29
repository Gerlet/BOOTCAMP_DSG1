#IMPUTS
print("Mi calculadora")
a=input("Ingrese un número por favor: ")
b=input("Ingrese otro número por favor: ")
operacion=input("Ingrese el tipo de operación por favor (suma|resta|multiplicación|división|potencia) ")
#PRCESO
if(operacion=="suma"):
    resultado=float(a)+float(b)
elif(operacion=="resta"):
    resultado=float(a)-float(b)    
elif(operacion=="multiplicación"):
    resultado=float(a)*float(b)    
elif(operacion=="división"):
    resultado=float(a)/float(b)
elif(operacion=="potencia"):
    resultado=float(a)**(float(b))        
else:
    print("Error")
    exit()
#OUTPUTS
print("El resultado es: ",resultado) 