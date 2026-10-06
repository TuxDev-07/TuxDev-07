print("------¿ES UN PALINDROMO?------")
cadena = input("Ingrese una cadena: ")
cadena_vacia = ""
for letra in range(len(cadena) -1 , -1 , -1):
    cadena_vacia = cadena_vacia + cadena[letra]
if cadena == cadena_vacia:
    print(cadena_vacia)
    print(f"La cadena: {cadena} es palindromo")
else:
    print(f"La cadena: {cadena} no es un palindromo")