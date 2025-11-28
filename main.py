import tkinter as tk
import random

from Characters import Personaje
from Guerrero import Guerrero
from mago import Mago

personajePrueba1 = Personaje(canvas="Canvas", nombre="Está esperando", x=10, y=10)
print(personajePrueba1.realizar_accion())

magoPrueba1 = Mago(canvas="Canvas", nombre="Lanza una bola de fuego", x=10, y=10)
print(magoPrueba1.realizar_accion())

guerreroPrueba1 = Guerrero(canvas="Canvas", nombre="Ataca fuertemente con su Espada", x=10, y=10)
print(guerreroPrueba1.realizar_accion())

def crear_guerrero():
    nombre = inputName.get() or "Guerrero Anónimo"
    x, y = obtener_posicion_random()

    nuevo_guerrero = Guerrero(escenario_canvas, nombre, x, y)
    nuevo_guerrero.dibujar()

    #lista_objetos.append(nuevo_guerrero)
    #self.log_label.config(text=f"Se ha instanciado un objeto Clase Guerrero: {nombre}")

def crear_mago():
    nombre = inputName.get() or "Mago Anónimo"
    x, y = obtener_posicion_random()

    # INSTANCIACIÓN: Aquí nace el objeto
    nuevo_mago = Mago(escenario_canvas, nombre, x, y)
    nuevo_mago.dibujar()

    #lista_objetos.append(nuevo_mago)
    #self.log_label.config(text=f"Se ha instanciado un objeto Clase Mago: {nombre}")

ventana = tk.Tk()
ventana.geometry("800x700")
frame_control = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frame_control.pack(fill=tk.X)
tk.Label(frame_control, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
inputName = tk.Entry(frame_control)
inputName.pack(side=tk.LEFT, padx=5)
tk.Button(frame_control, text="Crear Guerrero", bg="#e74c3c", fg="white",
          command=crear_guerrero).pack(side=tk.LEFT, padx=5)
tk.Button(frame_control, text="Crear Mago", bg="#3498db", fg="white",
          command=crear_mago).pack(side=tk.LEFT, padx=5)
#creamos una variable para poder dibujar sobre ella
escenario_canvas = (tk.Canvas(ventana, width=800, height=500, bg="#2c3e50"))
escenario_canvas.pack(fill=tk.BOTH, expand=True) #expand=True permite que crezca si la ventana cambia de tamañoventana.title("Demo Visual de POO - Mi Ventana")
labelAtaque = tk.label(ventana)
labelAtaque.pack(bg="#ecf0f1")


def obtener_posicion_random():
    """Genera coordenadas aleatorias dentro del canvas."""
    x = random.randint(50, 750)
    y = random.randint(50, 650)
    return x, y


ventana.mainloop()


