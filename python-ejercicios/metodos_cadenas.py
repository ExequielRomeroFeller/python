#dir() nos devuelve todos los métodos que se pueden trabajar con el parámetro que se pasa
cadena1 = "Soy Exequiel"
cadena2 = "como estás?"

print(dir(cadena1))

#upper() convierte a mayúsculas una cadena, lower() convierte a minúsculas
print(cadena1.upper())
print(cadena2.lower())

#capitalize() convierte solo la primera letra en mayúsculas
print(cadena2.capitalize())

#find() nos devuelve la posición en la que se encuentra el dato buscado
print(cadena1.find())
