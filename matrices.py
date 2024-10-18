from tkinter import messagebox

def gauss_jordan(matriz, resultados, umbral=1e-10):

    n = len(matriz)

    for i in range(n):
        # Buscar fila pivote
        max_valor = abs(matriz[i][i])
        fila_pivote = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > max_valor:
                max_valor = abs(matriz[k][i])
                fila_pivote = k

        # Intercambiar filas si es necesario
        if fila_pivote != i:
            matriz[i], matriz[fila_pivote] = matriz[fila_pivote], matriz[i]
            resultados[i], resultados[fila_pivote] = resultados[fila_pivote], resultados[i]

        # Verificar si el pivote es muy cercano a cero
        if abs(matriz[i][i]) < umbral:
            # Si el resultado correspondiente también es cercano a cero, el sistema es indeterminado
            if abs(resultados[i]) < umbral:
                messagebox.showinfo("Resultado", "El sistema es indeterminado y tiene infinitas soluciones.")
                return
            else:
                # Si no, es inconsistente
                messagebox.showerror("Error", "El sistema es inconsistente y no tiene solución.")
                return

        # Normalizar la fila pivote
        pivote = matriz[i][i]
        for j in range(i, n):
            matriz[i][j] /= pivote
        resultados[i] /= pivote

        # Hacer cero los elementos debajo del pivote
        for k in range(i + 1, n):
            factor = matriz[k][i]
            for j in range(i, n):
                matriz[k][j] -= factor * matriz[i][j]
            resultados[k] -= factor * resultados[i]

    # Revisar si alguna fila es completamente cero
    for i in range(n):
        fila_nula = all(abs(matriz[i][j]) < umbral for j in range(n))
        if fila_nula and abs(resultados[i]) < umbral:
            messagebox.showinfo("Resultado", "El sistema es indeterminado y tiene infinitas soluciones.")
            return

    # Calcular soluciones hacia atrás
    soluciones = [0] * n
    for i in range(n - 1, -1, -1):
        soluciones[i] = resultados[i]
        for j in range(i + 1, n):
            soluciones[i] -= matriz[i][j] * soluciones[j]
        
    return soluciones
