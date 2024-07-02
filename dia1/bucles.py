tabla= int(input("Ingrese la tabla de multiplicar por favor: "))
for contador in range (1,13,1):
    print(f"{tabla}*{contador}={tabla*contador}")

contador=1
while(contador<=12):
    print(f"{tabla}x{contador}={tabla*contador}")
    contador+=1