#Esto es una lista, almacena cualquier tipo de datos, se indexa por índices
lista = ["Una cadena", 45, True]
print (lista[0])

#Esto es una dupla, se diferencia con la lista en que no se pueden modificar los datos
tupla = ("Una cadena", 45, True)
print (tupla)

#Conjunto set, son iguales a las listas, pero no se pueden modificar los elementos ni guardan repetidos
conjunto = {"Una cadena", 45, True}
print(conjunto)

#Diccionario, permite referencia los índices con strings
diccionario = {
       'nombre' : "Exequiel",
       'apellido' : "Romero Feller",
       'altura' : 1.72
}

print(diccionario['nombre'])

