#INPUT
dinero=input("Ingrese tu dinero por favor: ")
convertidor=(input("Ingrese a que moneda desea cambiar (dolares|pesos argentinos) :"))
#PROCESO
dolar=float(dinero)*0.26
pesos_argen=float(dinero)*237.51
if(convertidor=="dolares"):
    retiro=float(dolar)
elif(convertidor=="pesos argentinos"):
    retiro=float(pesos_argen)
else:
    print("Error en la selección de convertidor")
    exit()
#OUTPUT
print("El cambio según la moneda que escogiste es: ",retiro)