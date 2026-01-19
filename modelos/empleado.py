class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario # Encapsulamiento (privado)

    def obtener_salario(self):
        return self.__salario

    def mostrar_datos(self):
        return f"Empleado: {self.nombre}"