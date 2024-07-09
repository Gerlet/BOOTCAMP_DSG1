class Persona:
    def __init__(self,nom,ema):
        self.nombre=nom
        self.email=ema

    def mostrar(self):
        print("="*50)
        print(f"Nombre : {self.nombre}")
        print(f"Email : {self.email}")


class Alumno(Persona):
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota=nota
    
    def mostrar(self):
        super().mostrar()
        print(f"Nota : {self.nota}")
class Profesor(Persona):
     def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad=esp

     def mostrar(self):
         super().mostrar()
         print(f"Especialidad : {self.especialidad}")
    
class Empleado(Persona):
    pass
        
alumno1=Alumno('gerardo','gerardo28@gmail.com',15)
alumno1.mostrar()
print(f"Nota : {alumno1.nota}")
profesor1=Profesor('cesar','cesar@gmail.com','base de datos')
profesor1.mostrar()
print(f"Especialidad : {profesor1.especialidad}")

empleado1=Empleado('Ana','ana@gmail.com')
empleado1.mostrar()