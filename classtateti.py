from classtablero import Tablero
from classjugador import Jugador

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = self.jugador1
        self.tablero = Tablero()


    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno_actual.ficha)
        ganador = self.tablero.hay_ganador()
        if ganador:
            print(f"\n¡Ganó {self.turno_actual.nombre} ({ganador})!")
            return True
        if self.tablero.esta_lleno():
            print("\n¡Empate!")
            return True
        self.turno_actual = self.jugador1 if self.turno_actual == self.jugador2 else self.jugador2
        return False