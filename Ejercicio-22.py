nota = float(input())
if nota < 0 or nota > 10:
    print("La nota que has introducido no está entre 0 y 10")
elif nota < 5:
    print(f"Has sacado un {nota} y has suspendido")
else:
    print(f"Has sacado un {nota} y has aprobado")
