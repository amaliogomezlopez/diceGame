import random

def lanzar_dado(num_caras=6):
    """Simula el lanzamiento de un dado con un número de caras especificado."""
    return random.randint(1, num_caras)

def lanzar_varios_dados(num_dados, num_caras=6):
    """Simula el lanzamiento de varios dados."""
    resultados = []
    for _ in range(num_dados):
        resultado = lanzar_dado(num_caras)
        resultados.append(resultado)
    return resultados

def main():
    print("Simulador de lanzamiento de dados")
    
    # Número de dados
    num_dados = int(input("¿Cuántos dados te gustaría lanzar? "))
    
    # Número de caras en cada dado
    num_caras = int(input("¿Cuántas caras tiene el dado? (Ejemplo: 6 para un dado normal) "))
    
    # Lanzar los dados
    resultados = lanzar_varios_dados(num_dados, num_caras)
    
    # Mostrar los resultados
    print(f"\nResultados del lanzamiento de {num_dados} dado(s) de {num_caras} caras:")
    for i, resultado in enumerate(resultados, 1):
        print(f"Dado {i}: {resultado}")

if __name__ == "__main__":
    main()
