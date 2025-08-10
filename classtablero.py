from excepciones import PosOcupadaException, PosNoValidaException

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # Verificar si la posición es válida (entre 0 y 2)
        if not (0 <= fil < 3 and 0 <= col < 3):
            raise PosNoValidaException((fil, col))
        # Verificar si está ocupada
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException((fil, col))

    def mostrar(self):
        for fila in self.contenedor:
            print(" | ".join(c if c else " " for c in fila))
            print("-" * 9)


    def hay_ganador(self):
    # Revisar filas
        for fila in self.contenedor:
            if fila[0] != "" and fila[0] == fila[1] == fila[2]:
                return fila[0]

    # Revisar columnas
        for col in range(3):
            if self.contenedor[0][col] != "" and self.contenedor[0][col] == self.contenedor[1][col] == self.contenedor[2][col]:
                return self.contenedor[0][col]

    # Diagonal principal
        if self.contenedor[0][0] != "" and self.contenedor[0][0] == self.contenedor[1][1] == self.contenedor[2][2]:
            return self.contenedor[0][0]

    # Diagonal secundaria
        if self.contenedor[0][2] != "" and self.contenedor[0][2] == self.contenedor[1][1] == self.contenedor[2][0]:
            return self.contenedor[0][2]

        return None
    
    def esta_lleno(self):
        return all(celda != "" for fila in self.contenedor for celda in fila)

