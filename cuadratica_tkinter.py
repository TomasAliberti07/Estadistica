import tkinter as tk
from tkinter import messagebox
from cuadratica import calcular_area_cuadratica, graficar_funcion
def iniciar_cuadratica():


 def validar_entrada(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        intervalo_inicio = float(intervalo_inicio)
        intervalo_fin = float(intervalo_fin)
        num_rectangulos = int(num_rectangulos)
        
        if a  == 0:
            raise ValueError("El coeficiente cuadrático no debe ser cero")

        # Validar que el número de rectángulos sea positivo
        if num_rectangulos <= 0:
            raise ValueError("El número de rectángulos debe ser un entero positivo.")
        
        # Validar que el intervalo sea correcto
        if intervalo_inicio >= intervalo_fin:
            raise ValueError("El inicio del intervalo debe ser menor que el fin del intervalo.")
        
        return a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos
    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))
        return None

 def obtener_parametros():
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    intervalo_inicio = entry_intervalo_inicio.get()
    intervalo_fin = entry_intervalo_fin.get()
    num_rectangulos = entry_num_rectangulos.get()
    
    validacion = validar_entrada(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)
    
    if validacion is not None:
        a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos = validacion
        
        suma_inferior, suma_superior, area_real, error = calcular_area_cuadratica(
            a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos
        )

        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, f"Suma inferior: {suma_inferior:.2f}\n")
        texto_resultado.insert(tk.END, f"Suma superior: {suma_superior:.2f}\n")
        texto_resultado.insert(tk.END, f"Área real: {area_real:.2f}\n")
        texto_resultado.insert(tk.END, f"Error de cálculo: {error:.2f}\n")

        graficar_funcion(a, b, c, intervalo_inicio, intervalo_fin, num_rectangulos)

 root = tk.Tk()
 root.title("Cálculo de área de una función cuadrática")
 root.configure(bg="#A7C6ED")

 label_a = tk.Label(root, text="Coeficiente cuadrático:", bg="#A7C6ED", fg="black")
 label_a.grid(row=0, column=0, padx=10, pady=10)
 entry_a = tk.Entry(root)
 entry_a.grid(row=0, column=1, padx=10, pady=10)

 label_b = tk.Label(root, text="Coeficiente lineal:", bg="#A7C6ED", fg="black")
 label_b.grid(row=1, column=0, padx=10, pady=10)
 entry_b = tk.Entry(root)
 entry_b.grid(row=1, column=1, padx=10, pady=10)

 label_c = tk.Label(root, text="Coeficiente independiente:", bg="#A7C6ED", fg="black")
 label_c.grid(row=2, column=0, padx=10, pady=10)
 entry_c = tk.Entry(root)
 entry_c.grid(row=2, column=1, padx=10, pady=10)

 label_intervalo_inicio = tk.Label(root, text="Inicio del intervalo:", bg="#A7C6ED", fg="black")
 label_intervalo_inicio.grid(row=3, column=0, padx=10, pady=10)
 entry_intervalo_inicio = tk.Entry(root)
 entry_intervalo_inicio.grid(row=3, column=1, padx=10, pady=10)

 label_intervalo_fin = tk.Label(root, text="Fin del intervalo:", bg="#A7C6ED", fg="black")
 label_intervalo_fin.grid(row=4, column=0, padx=10, pady=10)
 entry_intervalo_fin = tk.Entry(root)
 entry_intervalo_fin.grid(row=4, column=1, padx=10, pady=10)

 label_num_rectangulos = tk.Label(root, text="Número de rectángulos:", bg="#A7C6ED", fg="black")
 label_num_rectangulos.grid (row=5, column=0, padx=10, pady=10)
 entry_num_rectangulos = tk.Entry(root)
 entry_num_rectangulos.grid(row=5, column=1, padx=10, pady=10)

 boton_calcular = tk.Button(root, text="Calcular área", command=obtener_parametros,bg="#A7C6ED",fg="black")
 boton_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

 texto_resultado = tk.Text(root, width=30, height=5)
 texto_resultado.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

 root.mainloop()