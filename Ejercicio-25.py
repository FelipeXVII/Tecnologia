nota = float(input())
if nota >= 0 and nota < 5:
    print(f"Tu nota es un {nota}, has sacado un insuficiente")
elif nota >= 5 and nota < 6.5:
    print(f"Tu nota es un {nota}, has sacado un satisfactorio")
elif nota >= 6.5 and nota < 8.5:
    print(f"Tu nota es un {nota}, has sacado un notable")
elif nota >= 8.5 and nota <= 10:
    print(f"Tu nota es un {nota}, has sacado un excelente")
else:
    print("La nota que has introducido no está entre 0 y 10")
