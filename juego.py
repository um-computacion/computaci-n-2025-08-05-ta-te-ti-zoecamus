from classtateti import Tateti
from classjugador import Jugador


class Juego:
    def __init__(self):
        self.juego_actual = None

    def crear_jugadores(self):
        nombre1 = input("Nombre del Jugador 1 (X): ") or "Jugador 1"
        nombre2 = input("Nombre del Jugador 2 (O): ") or "Jugador 2"
        jugador1 = Jugador(nombre1, "X")
        jugador2 = Jugador(nombre2, "O")
        return jugador1, jugador2

    def iniciar(self):
        while True:
            jugador1, jugador2 = self.crear_jugadores()
            self.juego_actual = Tateti(jugador1, jugador2)
            self.jugar_partida()
            if not self.reiniciar():
                print("Fin TaTeTi")
                break

    def jugar_partida(self):
        while True:
            self.juego_actual.tablero.mostrar()
            jugador = self.juego_actual.turno_actual
            print(f"Turno de: {jugador.nombre} ({jugador.ficha})")
            try:
                fil = int(input("Ingrese fila (0-2): "))
                col = int(input("Ingrese columna (0-2): "))
                terminado = self.juego_actual.ocupar_una_de_las_casillas(fil, col)
                if terminado:
                    self.juego_actual.tablero.mostrar()
                    break
            except Exception as e:
                print(f"Error: {e}\n")

    def reiniciar(self):
        respuesta = input("\n¿Querés jugar otra vez? (s/n): ").lower()
        return respuesta == "s"