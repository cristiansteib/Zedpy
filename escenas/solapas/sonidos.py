__author__ = 'cristian'

import data
import pilas

class OpcSonido():
    def __init__(self,config):
        self.config=config
        self.vol()
        self.sound()
        self.music()
        tarea=pilas.mundo.agregar_tarea_siempre(1,self._ok)

    def vol(self):
        self.barra_volumen=pilas.interfaz.Deslizador(x=20,y=20)

    def sound(self):
        #TODO poner las rutas de las imagenes

        self.boton_sonido=pilas.actores.boton.Boton(x=200,y=432,ruta_normal='.png', ruta_press='.png', ruta_over='.png')
        self.boton_sonido.conectar_presionado(self._toggle_sonido)
        self.boton_sonido.conectar_sobre(self.boton_sonido.pintar_sobre)
        self.boton_sonido.conectar_normal(self._pintarbotonsonido)
        #self.boton.aprender(pilas.habilidades.Arrastrable)

    def _toggle_sonido(self):
        if self.config.sonido==True:
            self.config.sonido=False
        else:
            self.config.sonido=True
        self._pintarboton()

    def _pintarbotonsonido(self):
        if self.config.graficos==True:
            self.boton_sonido.pintar_presionado
        else:
            self.boton_sonido.pintar_normal

    def music(self):
     #TODO poner las rutas de las imagenes

        self.boton_musica=pilas.actores.boton.Boton(x=300,y=432,ruta_normal='.png', ruta_press='.png', ruta_over='.png')
        self.boton_musica.conectar_presionado(self._toggle_musica)
        self.boton_musica.conectar_sobre(self.boton_musica.pintar_sobre)
        self.boton_musica.conectar_normal(self._pintarbotonmusica)

    def _toggle_musica(self):
        if self.config.musica==True:
            self.config.musica=False
        else:
          self.config.musica=True
        self._pintarboton()

    def _pintarbotonmusica(self):
        if self.config.musica==True:
            self.boton_musica.pintar_presionado
        else:
            self.boton_musica.pintar_normal

    def _ok(self):
        self.config.volumen=int(self.barra_volumen.progreso)
        return True
