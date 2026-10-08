cadena = input("Ingrese una cadena: ")
cadena_vacia = ""

for i in range(len(cadena) - 1, -1, -1):
    cadena_vacia += cadena[i]

print(cadena_vacia)
