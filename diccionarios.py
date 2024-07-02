capitales={
    'Perú': 'Lima', 
    'Chile':'Santiago',
    'Colombia': 'Bogota',
    'Ecuador':'Quito'
}
pais=input("Ingrese el pais: ")
if pais in capitales:
    capital=capitales[pais]
    print(f"La capital de {pais} es {capital}")
    eliminarcapital=input("Desea eliminar la capital (si,no)? ")
    if eliminarcapital=="si":
        capitales.pop(pais)
        print(capitales)
else:
    print(f"No se encontro la capital del {pais}")
    nuevacapital=input(f"Ingrese la capital de {pais}: ")
    capitales.update({pais:nuevacapital})
    print(capitales)

