from Pelicula import Pelicula

if __name__ == "__main__":
    print()
    pelicula1 = Pelicula(6798455145, "Son como niños", 102, "Dennis Dugan")
    pelicula2 = Pelicula(6798455145, "Piratas del caribe", 143, "Gore Verbinsky")
    pelicula3 = Pelicula(4671927254, "El contador 1", 124, "Gavin O'connor")

    print(pelicula1)
    print(pelicula2)
    print(pelicula3)
    print()

    print("Prestar pelicula1:", pelicula1.prestar())
    print("Volver a prestar pelicula1:", pelicula1.prestar())
    print()

    print("Devolver pelicula1:", pelicula1.devolver())
    print("Volver a devolver pelicula1:", pelicula1.devolver())
    print()

    print(pelicula2.costo_reproduccion(300))
    print()

    print("Título original de pelicula3:", pelicula3.get_titulo())
    pelicula3.set_titulo("El contador 2")
    print("Nuevo título de pelicula3:", pelicula3.get_titulo())
    print()

    print("¿pelicula1 y pelicula3 tienen el mismo código?", pelicula1 == pelicula3)
    print("¿pelicula1 y pelicula2 tienen el mismo código?", pelicula1 == pelicula2)
