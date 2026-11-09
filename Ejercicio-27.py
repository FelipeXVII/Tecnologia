letra = input()
if letra.isnumeric():
    print("El valor introducido es un número")
elif letra.islower():
    print("La letra es minúscula")
else:
    print("La letra es mayúscula ¿?")
