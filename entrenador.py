from seleccion_futbol import Seleccion_futbol

class Entrenador(Seleccion_futbol):
    federacion:str  = str


    def __init__(self, name, last_name,category,federacion):
        super().__init__(name, last_name,category,federacion)
        self.federacion = federacion