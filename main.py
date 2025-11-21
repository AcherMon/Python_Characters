import tkinter as tk

from Characters import Personaje
from Guerrero import Guerrero
from mago import Mago

personajePrueba1 = Personaje(canvas="Canvas", nombre="Está esperando", x=10, y=10)
print(personajePrueba1.realizar_accion())

magoPrueba1 = Mago(canvas="Canvas", nombre="Lanza una bola de fuego", x=10, y=10)
print(magoPrueba1.realizar_accion())

guerreroPrueba1 = Guerrero(canvas="Canvas", nombre="Ataca fuertemente con su Espada", x=10, y=10)
print(guerreroPrueba1.realizar_accion())

ventana = tk.Tk()
ventana.title("Demo Visual de POO - Mi Ventana")
ventana.geometry("800x700")
frame_control = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frame_control.pack(fill=tk.X)
tk.Label(frame_control, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
ventana.mainloop()


