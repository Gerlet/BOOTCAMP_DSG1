dias=["lunes", "martes", "miercoles"]
print(dias[1])
#regresar valores a la lista

dias.append("jueves")
dias.append("viernes")
print(dias)
#eliminar valores de la lista
dias.pop(0)
print(dias)
print(dias[0:4])
dias[0]="domingo"
dias[1]="lunes"
dias[2]="martes"
dias[3]="miercoles"
print(dias)

for contador in range(len(dias)):
    print(dias[contador])

for dia in dias:
    print(dia)
