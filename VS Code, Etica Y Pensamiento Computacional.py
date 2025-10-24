# Calculadora que interpreta directamente una expresión como 2*7, 7-2 o 1+2

expresion = input("Escribe la operación (ej: 2*7, 7-2, 1+2): ")

# Buscar qué operación contiene la expresión
if "+" in expresion:
    num1, num2 = expresion.split("+")
    operacion = "+"
elif "-" in expresion:
    num1, num2 = expresion.split("-")
    operacion = "-"
elif "*" in expresion:
    num1, num2 = expresion.split("*")
    operacion = "*"
else:
    print("Operación no permitida. Usa +, - o *.")
    exit()

# Convertir los valores a números
num1 = int(num1)
num2 = int(num2)

# Validar que estén entre 0 y 9
if 0 <= num1 <= 9 and 0 <= num2 <= 9:
    if operacion == "+":
        print("El resultado es:", num1 + num2)
    elif operacion == "-":
        print("El resultado es:", num1 - num2)
    elif operacion == "*":
        print("El resultado es:", num1 * num2)
else:
    print("Error: Los números deben ser del 0 al 9.")
