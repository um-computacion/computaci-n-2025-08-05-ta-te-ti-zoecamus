import unittest

from classtablero import Tablero
from classtateti import Tateti
from classjugador import Jugador
from excepciones import PosOcupadaException, PosNoValidaException


class TestTablero(unittest.TestCase):
    def setUp(self):
        self.t = Tablero()

    def test_colocar_ficha_valida(self):
        self.t.poner_la_ficha(1, 2, "X")
        self.assertEqual(self.t.contenedor[1][2], "X")

    def test_fuera_de_rango_lanza_PosNoValida(self):
        with self.assertRaises(PosNoValidaException):
            self.t.poner_la_ficha(3, 0, "X")  # fila inválida
        with self.assertRaises(PosNoValidaException):
            self.t.poner_la_ficha(0, -1, "O")  # columna inválida

    def test_posicion_ocupada_lanza_PosOcupada(self):
        self.t.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            self.t.poner_la_ficha(0, 0, "O")

    # Ganador en distintas líneas 
    def test_ganador_en_fila(self):
        self.t.poner_la_ficha(1, 0, "X")
        self.t.poner_la_ficha(1, 1, "X")
        self.t.poner_la_ficha(1, 2, "X")
        self.assertEqual(self.t.hay_ganador(), "X")

    def test_ganador_en_columna(self):
        self.t.poner_la_ficha(0, 2, "O")
        self.t.poner_la_ficha(1, 2, "O")
        self.t.poner_la_ficha(2, 2, "O")
        self.assertEqual(self.t.hay_ganador(), "O")

    def test_ganador_en_diagonal_principal(self):
        self.t.poner_la_ficha(0, 0, "X")
        self.t.poner_la_ficha(1, 1, "X")
        self.t.poner_la_ficha(2, 2, "X")
        self.assertEqual(self.t.hay_ganador(), "X")

    def test_ganador_en_diagonal_secundaria(self):
        self.t.poner_la_ficha(0, 2, "O")
        self.t.poner_la_ficha(1, 1, "O")
        self.t.poner_la_ficha(2, 0, "O")
        self.assertEqual(self.t.hay_ganador(), "O")

    # Empate 
    def test_empate_tablero_lleno_sin_ganador(self):
        movs = [
            (0,0,"X"), (0,1,"O"), (0,2,"X"),
            (1,0,"X"), (1,1,"O"), (1,2,"O"),
            (2,0,"O"), (2,1,"X"), (2,2,"X"),
        ]
        for f, c, s in movs:
            self.t.poner_la_ficha(f, c, s)
        self.assertIsNone(self.t.hay_ganador())
        self.assertTrue(self.t.esta_lleno())


class TestTateti(unittest.TestCase):
    def setUp(self):
        j1 = Jugador("J1", "X")
        j2 = Jugador("J2", "O")
        self.game = Tateti(j1, j2)

    def test_cambia_turno_despues_de_jugada_valida(self):
        
        self.assertEqual(self.game.turno_actual.ficha, "X")
        self.game.ocupar_una_de_las_casillas(0, 0) 
        self.assertEqual(self.game.turno_actual.ficha, "O")  

    def test_detecta_ganador_y_termina(self):
        
        self.game.ocupar_una_de_las_casillas(0, 0)  
        self.game.ocupar_una_de_las_casillas(1, 0)  
        terminado = self.game.ocupar_una_de_las_casillas(0, 1)  
        self.assertFalse(terminado)  
        self.game.ocupar_una_de_las_casillas(1, 1)  
        terminado = self.game.ocupar_una_de_las_casillas(0, 2)  
        self.assertTrue(terminado)

    def test_empate(self):

        secuencia = [
            (0,0), (0,1), (0,2),
            (1,1), (1,0), (1,2),
            (2,1), (2,0), (2,2),
        ]
        terminado = False
        for f, c in secuencia:
            terminado = self.game.ocupar_una_de_las_casillas(f, c)
        self.assertTrue(terminado)

    def test_no_permite_sobrescribir(self):
        self.game.ocupar_una_de_las_casillas(2, 2)  
        with self.assertRaises(PosOcupadaException):
            self.game.ocupar_una_de_las_casillas(2, 2)  

    def test_posicion_invalida(self):
        with self.assertRaises(PosNoValidaException):
            self.game.ocupar_una_de_las_casillas(3, 0)  


if __name__ == "__main__":
    unittest.main()
