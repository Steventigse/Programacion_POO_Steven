from modelos.empleado import Empleado
from modelos.desarrollador import Desarrollador
from servicios.nomina import procesar_pago

def main():
    # 1. Crear instancias (Demostración de funcionamiento)
    emp_general = Empleado("Ana García", 1500)
    dev_senior = Desarrollador("Steven Tigse", 2500, "Python")

    # 2. Ejecutar lógica demostrando POO
    print("SISTEMA DE GESTIÓN DE EMPLEADOS\n")
    
    # Aquí se ve el polimorfismo en acción al pasar distintos tipos de objetos
    procesar_pago(emp_general)
    procesar_pago(dev_senior)

    # 3. Intento de acceso a atributo encapsulado (Dará error si se descomenta)
    # print(emp_general.__salario) # <--- Esto violaría la encapsulación

if __name__ == "__main__":
    main()