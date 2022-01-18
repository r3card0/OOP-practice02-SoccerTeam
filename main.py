from seleccion_futbol import Seleccion_futbol

if __name__=="__main__":
    print("Hola equipo")

    futbolista = Seleccion_futbol("Hugo","Sánchez","Futbolista")
    print(vars(futbolista))

    entrenador = Seleccion_futbol("Manuel","Vucetich","Entrenador")
    print(vars(entrenador))

    masajista = Seleccion_futbol("Nacho","Ambriz","Masajista")
    print(vars(masajista))