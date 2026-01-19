class Empleado:
    """Clase base que representa a un empleado general."""
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        # ENCAPSULACIÓN: Atributo privado (__salario). 
        # No se puede acceder directamente desde fuera de la clase.
        self.__salario = salario 

    def mostrar_informacion(self):
        """Método base para mostrar datos."""
        return f"Empleado: {self.nombre}"

    # Método para acceder al atributo encapsulado (Getter)
    def obtener_salario(self):
        return self.__salario

    def calcular_pago(self):
        """Método que será sobrescrito (Polimorfismo)."""
        return self.__salario