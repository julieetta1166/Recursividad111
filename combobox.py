Actividad:
Crear una opción para cada operación matemática básica (+,-,/,*)
import tkinter as tk

from tkinter import ttk

root= tk.Tk()
combo= ttk.Combobox( root, values= [ "uno", "dos" , "tres"  ] )
                                    
combo.current(0)
combo.pack()

root.mainloop()
