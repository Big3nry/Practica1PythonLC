peso_payaso = 112  
peso_muñeca = 75   

payasos = int(input("Introduce el número de payasos vendidos: "))
muñecas = int(input("Introduce el número de muñecas vendidas: "))

peso_total = (peso_payaso * payasos + peso_muñeca * muñecas) / 1000  # Convertir el peso a kilogramos

print(f"El peso total del paquete es: {peso_total} kg")