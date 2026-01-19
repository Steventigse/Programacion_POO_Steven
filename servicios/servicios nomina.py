def procesar_pago(empleado):
    """
    Función que demuestra polimorfismo: 
    Acepta cualquier objeto tipo Empleado y ejecuta su versión de los métodos.
    """
    print("--- Procesando Pago ---")
    print(empleado.mostrar_informacion())
    print(f"Monto final a depositar: ${empleado.calcular_pago()}")
    print("-" * 25)