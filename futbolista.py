from seleccion_futbol import Seleccion_futbol

class Futbolista(Seleccion_futbol):
    demarcacion:str = str
    jugarPartidos:str = str


    def __init__(self, name, last_name,category,demarcacion,jugarPartidos):
        super().__init__(name, last_name,category,demarcacion,jugarPartidos)
        self.demarcacion = demarcacion
        self.jugarPartidos


