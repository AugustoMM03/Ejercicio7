from claseViajeroFrecuente import ViajeroFrecuente as VF

if __name__ == '__main__':
    viajero1 = VF(210,32875738,'Juan','Perez',1000)

    valor1 = int(input("Ingrese un valor para comparar: "))
    #print (viajero1.getMillas() == valor1)
    #print (valor1 == viajero1.getMillas())
    igual1= viajero1 == valor1
    igual2 = valor1 == viajero1
    if (igual1 == igual2):
        print("La comparacion es valida ")
    else:
        print("La comparacion no es valida")

    viajero1 = valor1 + viajero1
    print(viajero1.getMillas())

    valor2 = int(input("Ingrese otro valor: "))
    viajero1 = valor2 - viajero1
    print(viajero1.getMillas())

