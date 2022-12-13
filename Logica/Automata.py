import itertools
import random

class Automata:
    def __init__(self, reglas, radix, limite, frases, frontera):
        """

        Parametros
        ----------
        reglas: String
            Conjunto de valores de salida que indica cómo evolucionarán los autómatas.

        radix: int
            el self.ruleeral sistema

        limite: int
            El limite ancho de los autómatas (máximo y mínimo self.ruleber de celdas).
        """
        self.frontera = frontera
        self.transiciones = {}
        self.reglas = reglas
        self.radix = radix
        self.limite = limite
        self.frases = frases
        #print(self.frontera)
        #print(self.frases)
        self.inicializar_automata()

    def inicializar_automata(self):
        """
        Inicializa el autómata asignando una tabla de transiciones usando radix, listaReglas y limite..
        """
        iter = [i for i in range(self.radix)]
        if self.reglas == 0 or self.reglas is None: #Si la listaReglas inicial es None ó 0 (no fue asignada por el usuario), entonces asigna una listaReglas aleatoria
            self.reglas = []
            self.reglas = [random.randint(0, len(iter) - 1) for i in range(0, self.radix ** 3)]
        else:
            self.convertir_regla(self.radix)
        #print(self.listaReglas)
        estados = itertools.product(iter, repeat=3) # Hace todas las combinaciones para cada estado posible, 27
        estados = set(estados)

        print("Reglas ", self.reglas)
        self.transiciones = dict(zip(sorted(estados), self.reglas))
        #print(len(self.transiciones), self.transiciones)


    def obtener_estado_siguiente(self, adyacenteIzquierdo, estadoActual, adyacenteDerecho):
        """
         Obtiene el siguiente estado buscando en la tabla de transiciones donde (adyacenteIzquierdo, estadoActual, adyacenteDerecho) es
         la clave en forma de tupla.

        Parametros.
        ----------
        adyacenteIzquierdo: int
            estado actual izquierdo adyacente

        estadoActual: int
            estado actual.

        adyacenteDerecho: int
            estado actual derecho adyacente

        Returno
        -------
        int
            el siguiente estado

        """
        if (adyacenteIzquierdo, estadoActual, adyacenteDerecho) not in self.transiciones:
            return 0
        else:
            siguiente_estado = self.transiciones[(adyacenteIzquierdo, estadoActual, adyacenteDerecho)]
        return siguiente_estado


    def obtener_frase_siguiente(self, frase_actual):
        if self.frontera == 1:
            return self.fronteraCircular(frase_actual)
        if self.frontera == 2:
            return self.fronteraEspejo(frase_actual)
        if self.frontera == 3:
            return self.fronteraValorFijo(frase_actual)


    #izquierdo inicial = final y derecho final = inicial
    def fronteraCircular(self, frase_actual):
        frase_siguiente = []

        for i in range(len(frase_actual)):
            adyacenteIzquierdo = frase_actual[i - 1]
            actual = frase_actual[i]

            if i == len(frase_actual) - 1:
                adyacenteDerecho = frase_actual[0]
            else:
                adyacenteDerecho = frase_actual[i + 1]

            estado_siguiente = self.obtener_estado_siguiente(adyacenteIzquierdo, actual, adyacenteDerecho)
            frase_siguiente.append(estado_siguiente)
            #print(adyacenteIzquierdo, estadoActual, adyacenteDerecho)
        return frase_siguiente


    #Inicial = inicial y final = final
    def fronteraEspejo(self, frase_actual):
        frase_siguiente = []

        for i in range(len(frase_actual)):
            if i == len(frase_actual) - len(frase_actual):
                adyacenteIzquierdo = frase_actual[i]
            else:
                adyacenteIzquierdo = frase_actual[i - 1]
            actual = frase_actual[i]

            if i == len(frase_actual) - 1:
                adyacenteDerecho = frase_actual[i]
            else:
                adyacenteDerecho = frase_actual[i + 1]

            estado_siguiente = self.obtener_estado_siguiente(adyacenteIzquierdo, actual, adyacenteDerecho)
            frase_siguiente.append(estado_siguiente)
            #print(adyacenteIzquierdo, estadoActual, adyacenteDerecho)
        return frase_siguiente


    #Valor fijo 0 y 1
    def fronteraValorFijo(self, frase_actual):
        siguiente_frase = []
        for i in range(len(frase_actual)):
            if i == len(frase_actual) - len(frase_actual):
                adyacenteIzquierdo = 0
            else:
                adyacenteIzquierdo = frase_actual[i - 1]
            act = frase_actual[i]

            if i == len(frase_actual) - 1:
                adyacenteDerecho = 1
            else:
                adyacenteDerecho = frase_actual[i + 1]

            estado_siguiente = self.obtener_estado_siguiente(adyacenteIzquierdo, act, adyacenteDerecho)
            siguiente_frase.append(estado_siguiente)
            #print(adyacenteIzquierdo, estadoActual, adyacenteDerecho)
        return siguiente_frase


    def convertir_regla(self, base):
        """
        Convierte listaReglas de autómatas a base n
        """
        if self.reglas == 0:
            return '0'
        self.rules = []

        """
            Posibles combinaciones de 0,1,2 = 27
            (3^27)-1 = 7625597484986
            20 casillas combinado 3 repitiendo = 1540 posibles reglas
            Entonces la regla 1 es [0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 2, 0, 2, 0, 1, 0, 2, 2, 1]
            Entonces la regla 1540 es [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        """
        self.reglas = round((self.reglas * 7625597484986) / 1540)

        while self.reglas:
            self.reglas, r = divmod(self.reglas, base)
            self.rules.append(str(r))

        while len(self.rules) < self.radix**3:
            self.rules.append("0")
        #return ''.join(reversed(self.rules))
        self.reglas = ''.join(reversed(self.rules))
        self.reglas = [int(r) for r in self.reglas]

