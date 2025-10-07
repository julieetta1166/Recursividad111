sumar dos numeros y mostrar resultado. Utilizar tkinter

import tkinter as tk
ventana=tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("400x300")

label=tk.Label(ventana, text="Ingresar numero: ", font=("Arial", 14))
label.pack()

entrada=tk.Entry(ventana)
entrada.pack()   #pide al usuario
texto=entrada.get() #obtener el valor

entrada=tk.Entry(ventana)
entrada.pack()   #pide al usuario
texto=entrada.get() #obtener el valor

def saludar():
    print("Resultado:")
boton=tk.Button(ventana, text="Suma",command=saludar)
boton.pack()


ventana.mainloop()
