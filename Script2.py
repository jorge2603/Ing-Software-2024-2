def calculavalle(cadena):
    cuentapasada=0
    cuentaactual=0
    valles=0
    for x in cadena:
        if x == "D":
            cuentapasada=cuentaactual
            cuentaactual-=1
        elif x == "U":
            cuentapasada=cuentaactual
            cuentaactual+=1
            if cuentaactual==0 and cuentapasada<0:
                valles+=1
    return valles






class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.hijo_izq=None
        self.hijo_der=None
        self.padre=None
        if self.padre==None:
            self.padre=self.valor
    
    def insertar(self,valor):
        if valor<self.padre:
            if self.hijo_izq==None:
                self.hijo_izq=Nodo(valor)
            else:
                self.hijo_izq.insertar(valor)
        else:
            if self.hijo_der==None:
                self.hijo_der=Nodo(valor)
            else:
                self.hijo_der.insertar(valor)

    def inorden(self,lista):
        if self.hijo_izq!=None:
            self.hijo_izq.inorden(lista)
        lista.append(self.valor)
        if self.hijo_der!=None:
            self.hijo_der.inorden(lista)

    def preorden(self,lista):
        lista.append(self.valor)
        if self.hijo_izq!=None:
            self.hijo_izq.preorden(lista)
        if self.hijo_der!=None:
            self.hijo_der.preorden(lista)

    def postorden(self,lista):
        if self.hijo_izq!=None:
            self.hijo_izq.postorden(lista)
        if self.hijo_der!=None:
            self.hijo_der.postorden(lista)
        lista.append(self.valor)


if __name__ == "__main__":
    bandera=True
    print("Que desea hacer: \n 1.-Calcular valles \n 2.-Arbol binario ordenado\n 3.- salir")
    respuesta=int(input())
    if respuesta==1:
        cadena=input("Ingrese la cadena: ")
        print(calculavalle(cadena))
    elif respuesta==2:
        while True:
            print("Que desea hacer: \n 1.-Insertar \n 2.-Inorden \n 3.-Preorden \n 4.-Postorden \n 5.-Salir")
            respuesta=int(input())
            if respuesta==1:
                if bandera:
                    arbol=Nodo(int(input("Ingrese el valor de la raiz: ")))
                    bandera=False
                else:
                    arbol.insertar(int(input("Ingrese el valor: ")))
            elif respuesta==2:
                listafinal=[]
                arbol.inorden(listafinal)
                print(listafinal)
            elif respuesta==3:
                listafinal=[]
                arbol.preorden(listafinal)
                print(listafinal)
            elif respuesta==4:
                listafinal=[]
                arbol.postorden(listafinal)
                print(listafinal)
            elif respuesta==5:
                break
