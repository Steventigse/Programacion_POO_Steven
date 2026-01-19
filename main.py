from modelos.empleado import Empleado
from modelos.desarrollador import Desarrollador
from servicios.nomina import calcular_pago

def ejecutar():
    persona = Empleado("Ana Lopez", 1200)
    programador = Desarrollador("Steven Tigse", 2500, "Python")

    print("--- PRUEBA DE POO EXITOSA ---")
    calcular_pago(persona)
    print("-" * 30)
    calcular_pago(programador)

if __name__ == "__main__":
    ejecutar()