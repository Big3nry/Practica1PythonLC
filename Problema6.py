edad = int(input("¿Cuál es tu edad? "))
if edad < 4:
    precio = 0
elif edad >= 4 and edad <= 18:
    precio = 5
else:
    precio = 10
print(f"El precio de la entrada es: ${precio}")