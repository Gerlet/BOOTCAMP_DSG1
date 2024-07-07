def suma(n1,n2):
    resultado=n1+n2
    return resultado

r1=suma(3,4)
r2=suma(10,r1)

print(r1)
print(r2)

#parametros ars y kwags:

def sumainfinito(*args):
    resulado=0
    for numero in args:
        resulado +=numero
    return resulado

r3=sumainfinito(3,4,5,10,20,10,21,24,535,3)

print(r3)

def calculadora(**kwargs):
    ope=kwargs.get('ope')
    n1=kwargs.get('n1')
    n2=kwargs.get('n2')

    if (ope=="suma"):
        resultado=n1+n2
    elif(ope=="resta"):
        resultado=n1-n2
    elif(ope=="mult"):
        resultado=n1*n2
    else:
        resultado="OPERACIÓN NCORRECTA"

    return resultado    

r5=calculadora(n1=5,n2=3,ope='mult')
print(r5)