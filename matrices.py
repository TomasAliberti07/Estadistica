from tkinter import messagebox

class ErrorMatriz(Exception):
    """Excepción personalizada para errores relacionados con la matriz."""
    pass

def gauss_jordan(matriz, resultados):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Jordan.

    Parámetros:
    matriz (list): Matriz cuadrada de coeficientes.
    resultados (list): Vector de resultados.

    Retorna:
    list: Soluciones del sistema de ecuaciones lineales.

    Levanta:
    ErrorMatriz: Si la matriz no es cuadrada o si hay división por 0.
    """

    # Verificación de entradas
    if len(matriz) != len(matriz[0]):
        raise ErrorMatriz("La matriz no es cuadrada.")
    if len(matriz) != len(resultados):
        raise ErrorMatriz("La cantidad de resultados no coincide con la cantidad de filas de la matriz.")

    n = len(matriz)
    for i in range(n):
        # Buscar fila pivote
        max_valor = abs(matriz[i][i])
        fila_pivote = i
        for k in range(i+1, n):
            if abs(matriz[k][i]) > max_valor:
                max_valor = abs(matriz[k][i])
                fila_pivote = k

        # Intercambiar filas si es necesario
        if fila_pivote != i:
            matriz[i], matriz[fila_pivote] = matriz[fila_pivote], matriz[i]
            resultados[i], resultados[fila_pivote] = resultados[fila_pivote], resultados[i]

        # Verificar si hay división por 0
        if matriz[i][i] == 0:
            messagebox.showerror("Error", "División por 0. El sistema no tiene solución, es incompatible.")
            return

        # Hacer cero los elementos debajo del pivote
        for k in range(i + 1, n):
            factor = matriz[k][i] / matriz[i][i]
            for j in range(i, n):
                matriz[k][j] -= factor * matriz[i][j]
            resultados[k] -= factor * resultados[i]

    # Calcular soluciones y verificar indeterminación o inconsistencia
    soluciones = [0] * n
    for i in range(n - 1, -1, -1):
        # Verificar si hay división por 0
        if matriz[i][i] == 0:
            if resultados[i] == 0:
                messagebox.showinfo("Resultado", "El sistema es indeterminado y tiene infinitas soluciones.")
                return
            else:
                messagebox.showerror("Error", "El sistema es inconsistente y no tiene solución.")
                return

        soluciones[i] = resultados[i]
        for j in range(i + 1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]
        soluciones[i] /= matriz[i][i]

    return soluciones