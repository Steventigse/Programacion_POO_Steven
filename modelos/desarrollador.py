from modelos.empleado import Empleado

class Desarrollador(Empleado): # Herencia
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_datos(self): # Polimorfismo
        return f"Desarrollador: {self.nombre}, Lenguaje: {self.lenguaje}"or especialidad