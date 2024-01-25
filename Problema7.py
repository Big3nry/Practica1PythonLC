numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Seleccione la operación que desea realizar:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
print("3. Mostrar la multiplicación de los dos números")

opcion = input("Opción: ")

if opcion == "1":
    print(f"La suma de {numero1} y {numero2} es: {numero1 + numero2}")
elif opcion == "2":
    print(f"La resta de {numero1} y {numero2} es: {numero1 - numero2}")
elif opcion == "3":
    print(f"La multiplicación de {numero1} y {numero2} es: {numero1 * numero2}")
else:
    print("Opción no válida")