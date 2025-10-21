Actividad:
Crear una opción para cada operación matemática básica (+,-,/,*)
import tkinter as tk

from tkinter import ttk

root= tk.Tk()
combo= ttk.Combobox( root, values= [ "uno", "dos" , "tres"  ] )
                                    
combo.current(0)
combo.pack()

root.mainloop()


import tkinter as tk
from tkinter import ttk

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora simple")
ventana.geometry("400x300")

# Etiqueta y primera entrada
label1 = tk.Label(ventana, text="Ingresa el primer número:", font=("Arial", 12))
label1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

# Etiqueta y segunda entrada
label2 = tk.Label(ventana, text="Ingresa el segundo número:", font=("Arial", 12))
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Combobox para seleccionar operación
label_op = tk.Label(ventana, text="Selecciona una operación:", font=("Arial", 12))
label_op.pack()

operaciones = ["+", "-", "*", "/"]
combo = ttk.Combobox(ventana, values=operaciones, state="readonly")
combo.current(0)  # Selecciona "+" por defecto
combo.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 14))
resultado_label.pack(pady=10)

# Función para realizar la operación
def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacion = combo.get()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                resultado = "Error: División por cero"
            else:
                resultado = num1 / num2
        else:
            resultado = "Operación no válida"

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Error: Ingresa números válidos")

# Botón para ejecutar
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack()

# Ejecutar ventana
ventana.mainloop()
