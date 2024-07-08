f = open('empresas.txt','w')
f.write('12345678910, SAGA FALABELLA SAC, JR LIMA 1025')
f.close()

fa = open('empresas.txt','a')
fa.write('\n')
fa.write('98765432110, RIPLEY , MANZANARES')
fa.close()

fr = open('empresas.txt','r')
data_empresas = fr.read()
print(data_empresas)
print(type(data_empresas))
fr.close()