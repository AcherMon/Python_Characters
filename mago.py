from Characters import Personaje

class Mago(Personaje):
    """Hereda de Personaje. Es otro tipo específico."""
    def __init__(self, canvas, nombre, x, y):
        super().__init__(canvas, nombre, x, y)
        self.color = "#e09994"
        self.mana = 100

    # POLIMORFISMO: Misma función, comportamiento diferente
    def realizar_accion(self):
        return f"¡{self.nombre} lanza un maleficio! (Maná: {self.mana})"