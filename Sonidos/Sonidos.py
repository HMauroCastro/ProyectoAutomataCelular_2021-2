import pygame
pygame.mixer.init()
pygame.mixer.set_num_channels(10)

listaBajos = []
listaCajaMusical = []
listaCampanas = []
listaFlautas = []
listaGuitarras = []
listaSintetizadores = []
listaViolines = []
listaVoces = []
listaBambus = []
listaTriangulos = []

listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass1.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass2.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass3.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass4.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass5.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass6.ogg"))
listaBajos.append(pygame.mixer.Sound(".\\Sonidos\\Bajo\\bass7.ogg"))

listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox1.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox2.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox3.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox4.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox5.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox6.ogg"))
listaCajaMusical.append(pygame.mixer.Sound(".\\Sonidos\\Caja musical\\musicBox7.ogg"))

listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell1.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell2.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell3.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell4.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell5.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell6.ogg"))
listaCampanas.append(pygame.mixer.Sound(".\\Sonidos\\Campana\\bell7.ogg"))

listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute1.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute2.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute3.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute4.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute5.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute6.ogg"))
listaFlautas.append(pygame.mixer.Sound(".\\Sonidos\\Flauta\\flute7.ogg"))

listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar1.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar2.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar3.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar4.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar5.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar6.ogg"))
listaGuitarras.append(pygame.mixer.Sound(".\\Sonidos\\Guitarra\\guitar7.ogg"))

listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer1.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer2.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer3.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer4.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer5.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer6.ogg"))
listaSintetizadores.append(pygame.mixer.Sound(".\\Sonidos\\Sintetizador\\synthesizer7.ogg"))

listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin1.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin2.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin3.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin4.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin5.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin6.ogg"))
listaViolines.append(pygame.mixer.Sound(".\\Sonidos\\Violin\\violin7.ogg"))

listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice1.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice2.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice3.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice4.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice5.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice6.ogg"))
listaVoces.append(pygame.mixer.Sound(".\\Sonidos\\Voz\\voice7.ogg"))

listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo1.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo2.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo3.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo4.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo5.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo6.ogg"))
listaBambus.append(pygame.mixer.Sound(".\\Sonidos\\Bambu\\bamboo7.ogg"))

listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Silencio\\silence.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles1.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles2.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles3.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles4.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles5.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles6.ogg"))
listaTriangulos.append(pygame.mixer.Sound(".\\Sonidos\\Triangulo\\triangles7.ogg"))
