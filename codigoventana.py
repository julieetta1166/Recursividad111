import tkinter as tk
ventana=tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("400x300")

label= tk.Label( ventana, text="Hola", font=("Arial", 14))
label.pack()

entrada=tk.Entry(ventana)
entrada.pack(pady=10)   #pide al usuario
texto=entrada.get() #obtener el valor

def saludar():
    print("Hola")
boton= tk.Button(ventana, text="Saludar", command=saludar)
boton.pack( )

ventana.mainloop()
