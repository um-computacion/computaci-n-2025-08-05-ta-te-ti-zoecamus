
class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre  # "Jugador 1"
        self.ficha = ficha    # "X" o "O"

    def __repr__(self):
        return f"{self.nombre} ({self.ficha})"