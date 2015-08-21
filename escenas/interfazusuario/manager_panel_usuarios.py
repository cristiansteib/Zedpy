__author__ = 'cristian'
"""


aca se maneja el panel con la lista de usuarios


"""

import pilas
import escenas

class InterfazUsuario(object):
    def __init__(self,lista):

        self.lista_de_nombre=lista
        self.lista_de_botones=[]

    def comenzar(self):

        y=300 #comienzo de la lista

        self.mono = pilas.actores.Mono()
        #self.mono.aprender(pilas.habilidades.SeguirClicks)

        self.mono.z = 1
        self.mono.escala=0
        self.mono.radio_de_colision=10
        self.mono.x=500
        self.mono.click_de_mouse(self.mover_al_mono)


        for elem in self.lista_de_nombre:
            self.m=pilas.actores.Texto(texto=elem,magnitud=55,fuente='./escenas/interfazusuario/AGENCYB.TTF')
            self.m.radio_de_colision=15
            self.lista_de_botones.append(self.m)
            y=y-75
            self.m.y=y
            self.m.x=-800
            self.m.z=-5

        pilas.escena_actual().colisiones.agregar(self.mono,self.lista_de_botones,self.cambiar_escena)


    def mover_al_mono(self,contexto):
        self.mono.x = contexto.x
        self.mono.y = contexto.y


    def cambiar_escena(self,mono,boton):
        self.mono.eliminar()


        pilas.cambiar_escena(escenas.escena_menu.iniciar(('existe',boton.texto)))








interfaz=InterfazUsuario




