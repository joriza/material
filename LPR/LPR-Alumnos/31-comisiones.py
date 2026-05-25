nombre = input("Dime tu nombre: ")
ventas = int(input("Por favor, ingresa el monto total de tus ventas: "))

comisiones = round(ventas * 13 / 100, 2)

print(f"El empleado {nombre} tiene una comisión de {comisiones}$")