var_numero = 6734
var_suma = 0
var_numero = str(var_numero)
var_longitud = len(var_numero)
var_suma = int(var_numero[0]) + int(var_numero[1]) + int(var_numero[2]) + int(var_numero[3])
if var_suma % 2 == 0:
    print(f"el valor de {var_suma} es par")
else:
    print(f"el valor de {var_suma} es impar")
