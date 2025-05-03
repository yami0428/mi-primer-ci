def suma(a, b):
    return a + b  # Corregido

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print("Calculadora básica")
    print(f"2 + 3 = {suma(2, 3)}")
    print(f"5 - 2 = {resta(5, 2)}")
    print(f"4 * 6 = {multiplicacion(4, 6)}")
    print(f"10 / 2 = {division(10, 2)}")