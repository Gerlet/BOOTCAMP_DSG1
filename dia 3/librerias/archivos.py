f = open('alumnos.txt','w')
f.write('Gerardo,elcoleccionista28gc@gmail.com,983762478')
f.close()

fa = open('alumnos.txt','a')
fa.write('\n')
fa.write('ana martinez,ana@gmail.com,89789897')
fa.close()

fr = open('alumnos.txt','r')
data_alumnos = fr.read()
print(data_alumnos)
print(type(data_alumnos))
fr.close()