num1 = float(input())
num2 = float(input())
if num1 < 0 or num1 > 10 or num2 < 0 or num2 > 10:
    print("Uno o los dos números están fuera de los limites establecidos")
elif num1 > num2:
    print(f"El número {num1:g} es mayor que el número {num2:g}")
elif num2 > num1:
    print(f"El número {num2:g} es mayor que el número {num1:g}")
else:
    print("Ambos números son iguales")
