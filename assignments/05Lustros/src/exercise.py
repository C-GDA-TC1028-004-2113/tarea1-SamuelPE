def main():
    #escribe tu código abajo de esta línea
    #Dame el año de nacimiento: 1998
    #Dame el año actual: 2021
    #Los lustros que has vivido son: 4.6
    
    nacimiento = int(input("Dame el año de nacimiento: "))
    actual = int(input("Dame el año actual: "))

    lustros = (actual - nacimiento)/5

    print("Los lustros que has vivido son: " + str(lustros))



if __name__ == '__main__':
    main()
