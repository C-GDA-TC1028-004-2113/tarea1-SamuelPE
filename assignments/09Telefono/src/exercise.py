def main():
    #escribe tu código abajo de esta línea
    #Dame el número de mensajes: 38
    #Dame el número de megas: 3.1
    #Dame el número de minutos: 78
    #El costo mensual es: 95.28

    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))

    costo = (mensajes + megas + minutos)*0.80

    print("El costo mensual es: " + str(costo))


if __name__ == '__main__':
    main()
