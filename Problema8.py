hora = input("Introduce la hora en formato HH:MM o MM:HH: ")
hours, minutes = hora.split(":")
hora_flotante = float(hours) + float(minutes) / 60
if hora_flotante >= 7 and hora_flotante <= 8:
    print("Es hora de desayunar")
elif hora_flotante >= 12 and hora_flotante <= 13:
    print("Es hora de almorzar")
elif hora_flotante >= 18 and hora_flotante <= 19:
    print("Es hora de cenar")
else:
    print("No es hora de comer")