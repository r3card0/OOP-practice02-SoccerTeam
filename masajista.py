from seleccion_futbol import Seleccion_futbol

class Masajista(Seleccion_futbol):
    titulacion:str          = int
    anios_experiencia:int   = int
    dar_masajes:str         = int


    def __init__(self, name, last_name,category,titulacion,anios_experiencia,dar_masajes):
        super().__init__(name, last_name,category,titulacion,anios_experiencia,dar_masajes)
        self.titulacion         = titulacion
        self.anios_experiencia  = anios_experiencia
        self.dar_masajes        = dar_masajes