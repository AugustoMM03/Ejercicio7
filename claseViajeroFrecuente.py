class ViajeroFrecuente:
    __numeroviajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasacumuladas = 0 
    def __init__(self, numeroviajero = 0, dni='', nombre='', apellido='', millasacumuladas=0):
        self.__numeroviajero = numeroviajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacumuladas = millasacumuladas
    
    def cantidadTotaldeMillas(self):
        return self.__millasacumuladas
    
    def acumularMillas(self, recorridas):
        self.__millasacumuladas += recorridas
        return self.__millasacumuladas

    def canjearMillas(self, canjear):
        if canjear > self.__millasacumuladas:
            print("Error en la operacion, no tiene millas suficientes para realizar el canje, tiene: ")
        else:
            self.__millasacumuladas -= canjear
            print("Millas canjeadas, le quedan: ")
        return self.__millasacumuladas

    def getNumViajero(self):
        return self.__numeroviajero
    
    def getMillas(self):
        return self.__millasacumuladas
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def __gt__(self, otroViajero):
        return ViajeroFrecuente(self.__millasacumuladas > otroViajero.getMillas()) 
    
    def __eq__(self, otro):
        return ViajeroFrecuente(self.__millasacumuladas == otro) 
    

    def __add__(self, otroViajero):
        return ViajeroFrecuente(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacumuladas + otroViajero.getMillas())

    def __sub__(self, otroViajero):
        return ViajeroFrecuente(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacumuladas - otroViajero.getMillas())
    
    def __radd__(self, otro):
        return ViajeroFrecuente(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacumuladas + otro)

    def __rsub__(self, otro):
        return ViajeroFrecuente(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacumuladas - otro)
