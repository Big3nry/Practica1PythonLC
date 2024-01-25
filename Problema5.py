num_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))
es_mayor_a_tres = num_shows > 3
if es_mayor_a_tres:
    print("Has visto más de 3 shows musicales")
else:
    print("Has visto 3 o menos shows musicales")