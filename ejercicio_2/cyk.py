import time

def cyk(cadena, gramatica):
    n = len(cadena)
    tabla = [[set() for j in range(n)] for i in range(n)]

    # llenar diagonal
    for i in range(n):
        for variable, producciones in gramatica.items():
            if cadena[i] in producciones:
                tabla[i][i].add(variable)

    # llenar tabla
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            for k in range(i, j):
                for variable, producciones in gramatica.items():
                    for prod in producciones:
                        if len(prod) == 2:
                            B, C = prod
                            if B in tabla[i][k] and C in tabla[k+1][j]:
                                tabla[i][j].add(variable)

    return "S" in tabla[0][n-1]


# Gramática en CNF
gramatica = {
    "S": ["AB", "BC"],
    "A": ["BA", "a"],
    "B": ["CC", "b"],
    "C": ["AB", "a"]
}

# Cadena larga
cadena = "ba" * 50

inicio = time.time()
resultado = cyk(cadena, gramatica)
fin = time.time()

print("Cadena:", cadena)
print("Resultado:", "Aceptada" if resultado else "Rechazada")
print("Tiempo CYK:", fin - inicio)
