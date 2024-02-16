import random
def Partido_Tenis():
    Jugador1=input("Ingrese el nombre del jugador 1: ")
    Jugador2=input("Ingrese el nombre del jugador 2: ")
    sinset=True
    while sinset:
        Sets=int(input("Indique el numero de sets a jugar: "))
        if Sets%2==1:
            sinset=False
        else:
            print("El numero de sets debe ser impar")
    setsjugador1=0
    setsjugador2=0
    juegosjugador1=0
    juegosjugador2=0
    puntosjugador1=0
    puntosjugador2=0
    saque=random.randint(1,2)
    print("Ahora se decidira el juego:")
    while setsjugador1<Sets//2+1 and setsjugador2<=Sets//2+1:
        print("hola Hola hola hol---------")
        bandera2=True
        while bandera2:
            if saque==1:
                print("se tiro una moneda y el jugador 1 sacara")
                saque=4
            elif saque==2:
                print("se tiro una moneda y el jugador 2 sacara")
                saque=3
            elif saque==3:
                print("El jugador 1 saca")
                saque=4
            elif saque==4:
                print("El jugador 2 saca")
                saque=3
            if (juegosjugador1+juegosjugador2)%2==1:
                print("Se realiza cambio de cancha")
            bandera=True
            while bandera:
                ganador=input("Ingrese el ganador del juego: ")
                if (ganador == Jugador1):
                    print("Punto para el jugador 1")
                    if puntosjugador2==4:
                        puntosjugador2-=1
                    puntosjugador1+=1
                elif (ganador == Jugador2):
                    print("Punto para el jugador 2")
                    if puntosjugador1==4:
                        puntosjugador1-=1
                    puntosjugador2+=1
                if puntosjugador1==4 and puntosjugador2<3:
                    print("El jugador 1 gano el juego")
                    juegosjugador1+=1
                    bandera=False
                    puntosjugador1=0
                    puntosjugador2=0
                elif puntosjugador2==4 and puntosjugador1<3:
                    print("El jugador 2 gano el juego")
                    juegosjugador2+=1
                    bandera=False
                    puntosjugador1=0
                    puntosjugador2=0
                elif puntosjugador1==5:
                    print("El jugador 1 gano el juego")
                    juegosjugador1+=1
                    bandera=False
                    puntosjugador1=0
                    puntosjugador2=0
                elif puntosjugador2==5:
                    print("El jugador 2 gano el juego")
                    juegosjugador2+=1
                    bandera=False
                    puntosjugador1=0
                    puntosjugador2=0
                if juegosjugador1>=6 and abs(juegosjugador1-juegosjugador2)>=2:
                        setsjugador1+=1
                        juegosjugador1=0
                        juegosjugador2=0
                        print("El jugador1 gano 1 set")
                        bandera2=False

                if juegosjugador2>=6 and abs(juegosjugador1-juegosjugador2)>=2:
                        setsjugador2+=1
                        juegosjugador1=0
                        juegosjugador2=0
                        print("El jugador2 gano 1 set")
                        bandera2=False
                        
                print("\n El marcador es el siguiente: \n Jugador 1:", calculapuntos(puntosjugador1), "puntos \n Jugador 2:", calculapuntos(puntosjugador2), "puntos\n Jugador 1:", juegosjugador1, "juegos \n Jugador 2:", juegosjugador2, "juegos\n Jugador 1:", setsjugador1, "sets \n Jugador 2:", setsjugador2, "sets\n")
                    
        if setsjugador2==(Sets//2)+1:
            print("El ganador es: ",Jugador2)
        if setsjugador1==(Sets//2)+1:
            print("El ganador es: ",Jugador1)
        

def calculapuntos(puntaje):
    if puntaje==0:
        return "0"
    elif puntaje==1:
        return "15"
    elif puntaje==2:
        return "30"
    elif puntaje==3:
        return "40"
    elif puntaje==4:
        return "Adv"


Partido_Tenis()

