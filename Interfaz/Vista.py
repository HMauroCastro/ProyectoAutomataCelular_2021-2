from Interfaz.Cuadricula import Cuadricula
import Logica.Constantes as c
from Logica.Automata import Automata
import pygame
import Sonidos.Sonidos as sound
import sys
import random

class pygWindow:
    def __init__(self, temporizador, base, reglas, estados1, estados2, estados3, instrumentos, limite, frontera):
        pygame.init()
        pygame.display.set_caption('Automata')
        self.surface = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        self.surface.fill(c.BLACK)
        self.cuadricula1 = Cuadricula(20, 20, 40, 20, 15, 15)
        self.cuadricula2 = Cuadricula(460, 20, 40, 20, 15, 15)
        self.cuadricula3 = Cuadricula(900, 20, 40, 20, 15, 15)

        self.instrumentos = instrumentos

        self.reloj = pygame.time.Clock()
        self.temporizador = temporizador
        self.repaint_evt = pygame.USEREVENT + 1
        self.sound_evt = pygame.USEREVENT + 2

        if len(estados1) == 1 and estados1[0] == 0:
            estados1 = self.estados_random()
        if len(estados2) == 1 and estados2[0] == 0:
            estados2 = self.estados_random()
        if len(estados3) == 1 and estados3[0] == 0:
            estados3 = self.estados_random()

        print("Iniciales", estados1, estados2, estados3)

        self.automata1 = Automata(reglas, base, limite, estados1, frontera)
        self.automata2 = Automata(reglas, base, limite, estados2, frontera)
        self.automata3 = Automata(reglas, base, limite, estados3, frontera)
        self.iterador1 = 0
        self.iterador2 = 22
        self.iterador3 = 44
        self.j = 0

        pygame.time.set_timer(self.repaint_evt, temporizador)
        pygame.time.set_timer(self.sound_evt, temporizador + 2)


    def estados_random(self):
        iteraciones = [i for i in range(3)]
        estados = [random.randint(0, len(iteraciones) - 1) for i in range(0, 20)]
        return estados


    def manejo_eventos(self):
        """
        Maneja todos los eventos de pygame necesarios.
        """
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evt.type == self.repaint_evt:
                self.dibujar_cosas()
            elif evt.type == self.sound_evt:
                self.reproducir_sonidos()
            else:
                pass
              
    def dibujar_cosas(self):
        """
        """
        if self.iterador1 < self.cuadricula1.cols:
            if self.iterador1 < len(self.automata1.frases):
                validar_cuadro1 = self.automata1.frases[self.iterador1]
                validar_cuadro2 = self.automata2.frases[self.iterador1]
                validar_cuadro3 = self.automata3.frases[self.iterador1]
                self.iterador1 = self.cuadricula1.repintar_cuadro(self.surface, self.iterador1, validar_cuadro1)
                self.iterador2 = self.cuadricula2.repintar_cuadro(self.surface, self.iterador2, validar_cuadro2)
                self.iterador3 = self.cuadricula3.repintar_cuadro(self.surface, self.iterador3, validar_cuadro3)
                #print(i1, i2, i3)
                #self.reproducir_sonidos(i1, i2, i3)

            if self.iterador1 == self.cuadricula1.cols:
                self.cuadricula1.current_row += 1
                self.cuadricula2.current_row += 1
                self.cuadricula3.current_row += 1
            
        else:
            self.iterador1 = 0
            self.iterador2 = 22
            self.iterador3 = 44
            self.automata1.frases = self.automata1.obtener_frase_siguiente(self.automata1.frases)
            self.automata2.frases = self.automata2.obtener_frase_siguiente(self.automata2.frases)
            self.automata3.frases = self.automata3.obtener_frase_siguiente(self.automata3.frases)
            print("Siguientes", self.automata1.frases, self.automata2.frases, self.automata3.frases)

        
    def reproducir_sonidos(self):
        #lista de sonidos de cada instrumento musical son 7, el 0 es silencio
        list1 = [0, 1, 2, 3, 4, 5, 6, 7]
        r1 = random.choice(list1)
        r2 = random.choice(list1)
        r3 = random.choice(list1)

        if self.iterador1 < len(self.automata1.frases):
            i1 = self.automata1.frases[self.iterador1]
            i2 = self.automata2.frases[self.iterador1]
            i3 = self.automata3.frases[self.iterador1]

            i1=r1
            i2=r2
            i3=r3

        else:
            i1 = random.choice(list1)
            i2 = random.choice(list1)
            i3 = random.choice(list1)

        aux1 = False #si i1 fue usado
        aux2 = False #si i2 fue usado
        aux3 = False #si i3 fue usado

        #print("sonidos  ", i1, i2, i3)

        if 'Bamboo' in self.instrumentos:
            pygame.mixer.Channel(0).play(sound.listaBambus[i1])
            aux1 = True
        if 'Bass' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(1).play(sound.listaBajos[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(1).play(sound.listaBajos[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(1).play(sound.listaBajos[i3])
                aux3 = True
        if 'Bell' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(2).play(sound.listaCampanas[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(2).play(sound.listaCampanas[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(2).play(sound.listaCampanas[i3])
                aux3 = True
        if 'Flute' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(3).play(sound.listaFlautas[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(3).play(sound.listaFlautas[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(3).play(sound.listaFlautas[i3])
                aux3 = True
        if 'Guitar' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(4).play(sound.listaGuitarras[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(4).play(sound.listaGuitarras[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(4).play(sound.listaGuitarras[i3])
                aux3 = True
        if 'MusicBox' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(5).play(sound.listaCajaMusical[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(5).play(sound.listaCajaMusical[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(5).play(sound.listaCajaMusical[i3])
                aux3 = True
        if 'Synthesizer' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(6).play(sound.listaSintetizadores[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(6).play(sound.listaSintetizadores[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(6).play(sound.listaSintetizadores[i3])
                aux3 = True
        if 'Triangles' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(7).play(sound.listaTriangulos[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(7).play(sound.listaTriangulos[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(7).play(sound.listaTriangulos[i3])
                aux3 = True
        if 'Violin' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(8).play(sound.listaViolines[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(8).play(sound.listaViolines[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(8).play(sound.listaViolines[i3])
                aux3 = True
        if 'Voice' in self.instrumentos:
            if not aux1:
                pygame.mixer.Channel(9).play(sound.listaVoces[i1])
                aux1 = True
            elif not aux2:
                pygame.mixer.Channel(9).play(sound.listaVoces[i2])
                aux2 = True
            elif not aux3:
                pygame.mixer.Channel(9).play(sound.listaVoces[i3])
                aux3 = True
