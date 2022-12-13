import Logica.Constantes as cons
import pygame

class Cuadricula:
    def __init__(self, iniX, iniY, rows, cols, width, height, margin=5):
        self.iniX = iniX
        self.iniY = iniY
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.margin = margin
        self.boxes = {}
        self.current_row = 0
        #self.paint_evt = pygame.USEREVENT + 1

    def dibujar_cuadricula(self, surface):

        y = self.iniY
        for r in range(self.rows):
            x = self.iniX
            for c in range(self.cols):
                self.boxes.update({(x, y): 0})
                pygame.draw.rect(surface, cons.WHITE, (x, y, self.width, self.height))
                x += self.width + self.margin
            y += self.height + self.margin
        pygame.display.update()


    def repintar_cuadro(self, surface, i, color_key):
        """
        Repinta un cuadro de la cuadricula
        """
        x = (i+1)*self.width + (i+1)*self.margin
        y = (self.current_row+1)*self.height + (self.current_row+1)*self.margin
        pygame.draw.rect(surface, cons.color_keys[color_key], (x, y, self.width, self.height))
        pygame.display.update((x, y, self.width, self.height))
        i += 1
        return i

    def repintar_fila(self, surface, color_key_list):
        """
        repinta una fila de la cuadricula.

        Parametros
        ----------
        surface: pygame.display
            la superficie para pintar.

        color_key_list: list
            La lista que tiene los colores para pintar cada cuadro.
        """
        for i in range(len(color_key_list)):
            x = (i+1)*self.width + (i+1)*self.margin
            y = (self.current_row+1)*self.height + (self.current_row+1)*self.margin
            color_key = color_key_list[i]
            color = cons.color_keys[color_key]
            pygame.draw.rect(surface, color, (x, y, self.width, self.height))
            pygame.display.update()
        self.current_row += 1