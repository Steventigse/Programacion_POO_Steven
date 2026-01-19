from modelos.empleado import Empleado

# HERENCIA: Desarrollador hereda de Empleado
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        # Uso de super() para heredar atributos de la clase base
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    # POLIMORFISMO: Sobrescribimos el método mostrar_informacion
    def mostrar_informacion(self):
        return f"Desarrollador: {self.nombre}, Experto en: {self.lenguaje}"

    # POLIMORFISMO: Sobrescribimos el cálculo de pago (ej. bono por lenguaje)
    def calcular_pago(self):
        salario_base = self.obtener_salario()
        return salario_base + 500  # Bono fijo por especialidad