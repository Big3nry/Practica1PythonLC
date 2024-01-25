monto_consumo = float(input("¿Cuánto fue su consumo en el restaurante? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar? "))
propina = monto_consumo * (porcentaje_propina / 100)
print(f"La cantidad a dejar como propina es: {propina:.2f} dólares")