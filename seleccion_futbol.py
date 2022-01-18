class Seleccion_futbol():
    id: int         = str
    name: str       = str
    last_name:str   = str
    age: int        = str
    category:str    = str
    meet: str       = str
    travel: str     = str


    def __init__(self,name,last_name,category):
        self.name       = name
        self.last_name  = last_name
        self.category   = category