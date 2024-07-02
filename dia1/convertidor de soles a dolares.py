#INPUT
dinero=input("Ingrese tu dinero por favor: ")
convertidor=(input("Ingrese a que moneda desea cambiar (dolares|soles) :"))
#PROCESO
dolar=float(dinero)*0.26
sol=float(dinero)*3.85
if(convertidor=="dolares"):
    retiro=float(dolar)
elif(convertidor=="soles"):
    retiro=float(sol)
else:
    print("Error en la selección de convertidor")
    exit()
#OUTPUT
print("El cambio según la moneda que escogiste es: ",retiro)
