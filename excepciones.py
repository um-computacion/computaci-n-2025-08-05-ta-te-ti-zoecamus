class PosOcupadaException(Exception):
    def __init__(self, posicion=None):
        mensaje = f"Posición ya ocupada: {posicion}" if posicion else "Posición ya ocupada"
        super().__init__(mensaje)

class PosNoValidaException(Exception):
    def __init__(self, posicion=None):
        mensaje = f"Posición no válida: {posicion}" if posicion else "Posición no válida"
        super().__init__(mensaje)
