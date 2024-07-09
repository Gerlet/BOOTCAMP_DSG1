class Usuario:
    __email='elcoleccionista28gc@gmail.com'
    __pasword='hola1234'

    def __init__(self):
        pass

    def login(self,email,pasword):
        if(self.__email==email and self.__pasword == pasword):
            print(f"Bienvenido {self.__email}")
        
        else:
            print('datos incorrectos')

print("Login de usuarios")
email=input("Ingresa email: ")
pasword=input("Ingrese pasword: ")

usuario=Usuario()
#print(usuario.pasword)
#usuario.pasword="123"
usuario.login(email,pasword)