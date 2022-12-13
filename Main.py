##############################IMPORTS##############################

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from Interfaz.Vista import pygWindow

##############################GLOBALES##############################


listaInstrumentos = []
listaEstados1 = []
listaEstados2 = []
listaEstados3 = []
listaReglas = []
limite = 0
base = 0
intervaloTiempo = 0
frontera = 0

##############################INTERFAZ##############################


class WindowPQ(QMainWindow):
    def __init__(self):
        #1,1,1,2,1,2,1,0,0,0
        # iniciar pbjeto QMainWindow
        QMainWindow.__init__(self)
        # Cargar archivo
        uic.loadUi("Interfaz\\Automata.ui", self)
        # 0,1,1,1,2,1,0,0,0,2
        self.initUI()

    def initUI(self):
        self.addInstruments.clicked.connect(lambda: self.retornarInstrumentos())
        self.addState.clicked.connect(lambda: self.lista_estado())
        self.start.clicked.connect(
            lambda: self.setup(
                intervaloTiempo,
                base,
                listaReglas,
                listaEstados1,
                listaEstados2,
                listaEstados3,
                listaInstrumentos,
                limite,
                frontera
            )
        )
#0,1,2,1,0,1,2,0,1,2
    def retornarLista(self, string):
        string_list = string.split(",")
        int_list = []
        for i in string_list:
            int_list.append(int(i))
        return int_list

    def lista_estado(self):
        global listaEstados1
        global listaEstados2
        global listaEstados3
        global listaReglas
        global limite
        global base
        global intervaloTiempo
        global frontera

        listaReglas = int(self.inputRule.text())
        limite = 20
        base = 3
        intervaloTiempo = int(self.interval.text())
        listaEstados1 = self.retornarEstados(self.state1.text())
        listaEstados2 = self.retornarEstados(self.state2.text())
        listaEstados3 = self.retornarEstados(self.state3.text())
        frontera = self.tipoFrontera()


    def retornarEstados(self, string):
        lista_estados = []
        lista_estados = self.retornarLista(string)
        return lista_estados

    def tipoFrontera(self):
        if self.Circular.isChecked():
            return 1
        if self.Espejo.isChecked():
            return 2
        if self.ValorFijo.isChecked():
            return 3

    def retornarInstrumentos(self):
        instrumentos = []
        if self.Bamboo.isChecked():
            instrumentos.append("Bamboo")
        if self.Bass.isChecked():
            instrumentos.append("Bass")
        if self.Bell.isChecked():
            instrumentos.append("Bell")
        if self.Flute.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("Flute")
        if self.Guitar.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("Guitar")
        if self.MusicBox.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("MusicBox")
        if self.Synthesizer.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("Synthesizer")
        if self.Triangles.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("Triangles")
        if self.Violin.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("Violin")
        if self.Voice.isChecked():
            if len(instrumentos) < 4:
                instrumentos.append("Voice")
        global listaInstrumentos
        listaInstrumentos = instrumentos
        #print(listaInstrumentos)

    def setup(
        self,
        temporizador,
        base,
        reglas,
        estados1,
        estados2,
        estados3,
        sonidos,
        limite,
        frontera
    ):
        """
		Instances the pygame window and creates the main loop.
		"""
        window = pygWindow(
            temporizador,
            base,
            reglas,
            estados1,
            estados2,
            estados3,
            sonidos,
            limite,
            frontera
        )
        # text, None, [0,1,2,1,1,0,2,0,1,2], [0,1,2,1,1,0,2,0,1,2], [0,1,2,1,1,0,2,0,1,2], None, None, None, 10)
        window.cuadricula1.dibujar_cuadricula(window.surface)
        window.cuadricula2.dibujar_cuadricula(window.surface)
        window.cuadricula3.dibujar_cuadricula(window.surface)

        while True:
            window.reloj.tick(40)
            # window.dibujar_cosas()
            window.manejo_eventos()


app = QApplication(sys.argv)
_window = WindowPQ()
_window.show()
app.exec_()

