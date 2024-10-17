import tkinter as tk
from estadisticos_tkinter import root
from matrices_tkinter import root
from cuadratica_tkinter import root
def main():
    root = tk.Tk()
    root.title("Menú principal")
    root.geometry("800x200")  # Tamaño de la ventana
    root.configure(bg='lightgray')
    # Crear botones
    estadistica_button = tk.Button(root, text="Estadística", command=root)
    matrices_button = tk.Button(root, text="Matrices", command=root)
    funcion_cuadratica_button = tk.Button(root, text="Función Cuadrática", command=root)

    # Layout
    estadistica_button.grid(row=0, column=0, padx=5, pady=5)
    matrices_button.grid(row=1, column=0, padx=5, pady=5)
    funcion_cuadratica_button.grid(row=2, column=0, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()