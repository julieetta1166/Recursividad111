import tkinter as tk
ventana=tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("400x300")

label=tk.Label(ventana, text="Ingresar numero: ", font=("Arial", 14))
label.pack()

entrada=tk.Entry(ventana)
entrada.pack()   

entrada2=tk.Entry(ventana)
entrada2.pack()   

def saludar():
    num1 = float(entrada.get())
    num2 = float(entrada2.get())
    suma = num1 + num2
    print(suma)
boton=tk.Button(ventana, text="Suma",command=saludar)
boton.pack()

ventana.mainloop()
