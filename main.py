# 1. DEFINICIÓN DE LA LÓGICA (Proceso)
def calcular(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2 if n2 != 0 else "Error: División por cero"
    else:
        return "Operación no válida"

# 2. ENTRADA DE DATOS (Solo una vez)
print("--- Calculadora Simple ---")
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
operacion = input("Digite la operación (+, -, *, /): ")

# 3. SALIDA DE RESULTADOS
resultado = calcular(numero1, numero2, operacion)
print("----------------------------")
print(f"El resultado final es: {resultado}")