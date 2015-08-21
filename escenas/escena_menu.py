__author__ = 'cristian'
import pilas
import escenas
import data
import duinobot


class EscenaDeMenu(pilas.escena.Base):
    def __init__(self, lista):
        print 'haber'
        print lista
        self.jugador_nombre = lista[1]

        self.ls=lista
        pilas.escena.Base.__init__(self)
        print '{0} jugador {1}'.format(lista[0], lista[1])

        self.jugador = data.Jugador()

        if lista[0] == 'existe':
            self.existe=True
            self.jugador.nombre = lista[1]
            self.jugador.niveldatos=self.jugador.nivelmax  # esto es para que siga jugando a partir del nivel en q q termino

            escenas.datosplayer(self.jugador)

        else:
            self.existe=False
            self.jugador.JugadorNuevo = (self.jugador_nombre)


    def iniciar(self):
        p = pilas.actores.Sonido()
        self.chapa = pilas.actores.Actor(imagen='imag/escmenu/Inicio-4.png', x=-1500, y=0)
        self.chapa.escala = 1
        self.fondo = pilas.fondos.Fondo("./imag/Interfaz/fondo.png")

        self.chapa.x = pilas.interpolar(0, tipo='rebote_final', demora=1, duracion=2)
        self.bot = 1
        self.tarea = pilas.mundo.agregar_tarea(0.1, self.condicion)

    def condicion(self):
        c = True
        if self.chapa.x == 0:
            c = self.tarea_eve = pilas.mundo.agregar_tarea(1, self.event_botones)
        if c == False:
            return False
        else:
            return True

    def event_botones(self):
        if self.bot == 1:
            self.boton_jugar = pilas.actores.boton.Boton(x=-740, y=230, ruta_normal='imag/escmenu/jugar1.png',
                                                         ruta_press='imag/escmenu/jugar2.png', ruta_over='imag/escmenu/jugar2.png')
            self.boton_jugar.conectar_presionado(self.comenzar)
            self.boton_jugar.conectar_sobre(self.boton_jugar.pintar_presionado)
            self.boton_jugar.conectar_normal(self.boton_jugar.pintar_normal)
            self.boton_jugar.escala = 0.1
            self.boton_jugar.escala = [1], 0.1
            self.bot = self.bot + 1
            return True

        if self.bot == 3:

            self.boton_ayuda = pilas.actores.boton.Boton(x=-740, y=80, ruta_normal='imag/escmenu/aprender1.png',ruta_press='imag/escmenu/aprender2.png', ruta_over='imag/escmenu/aprender2.png')
            self.boton_ayuda.conectar_presionado(self.ayuda)
            self.boton_ayuda.conectar_sobre(self.boton_ayuda.pintar_presionado)
            self.boton_ayuda.conectar_normal(self.boton_ayuda.pintar_normal)
            self.boton_ayuda.escala = 0.1
            self.boton_ayuda.escala = [1], 0.1
            self.bot = self.bot + 1
            return True



        if self.bot == 5:
            self.boton_opc = pilas.actores.boton.Boton(x=-740, y=-70, ruta_normal='imag/escmenu/opciones1.png',
                                                       ruta_press='imag/escmenu/opciones2.png', ruta_over='imag/escmenu/opciones2.png')
            self.boton_opc.conectar_presionado(self.opciones)
            self.boton_opc.conectar_sobre(self.boton_opc.pintar_presionado)
            self.boton_opc.conectar_normal(self.boton_opc.pintar_normal)
            self.boton_opc.escala = 0.1
            self.boton_opc.escala = [1], 0.1
            self.bot = self.bot + 1
            return True


        if self.bot == 6:
            self.boton_estadistica = pilas.actores.boton.Boton(x=-740, y=-220, ruta_normal='imag/escmenu/estadisticas1.png',
                                                               ruta_press='imag/escmenu/estadisticas2.png',
                                                               ruta_over='imag/escmenu/estadisticas2.png')
            self.boton_estadistica.conectar_presionado(self.comenzar)
            self.boton_estadistica.conectar_sobre(self.boton_estadistica.pintar_presionado)
            self.boton_estadistica.conectar_normal(self.boton_estadistica.pintar_normal)
            self.boton_estadistica.escala = 0.1
            self.boton_estadistica.escala = [1], 0.1
            self.bot = self.bot + 1
            return True

        if self.bot == 9:
            self.boton_salir = pilas.actores.boton.Boton(x=-740, y=-370, ruta_normal='imag/escmenu/salir1.png',
                                                         ruta_press='imag/escmenu/salir2.png', ruta_over='imag/escmenu/salir2.png')
            self.boton_salir.conectar_presionado(self.salir)
            self.boton_salir.conectar_sobre(self.boton_salir.pintar_presionado)
            self.boton_salir.conectar_normal(self.boton_salir.pintar_normal)
            self.boton_salir.escala = 0.1
            self.boton_salir.escala = [1], 0.1
            self.bot = self.bot + 1

            return True


        elif self.bot < 12:
            self.bot = self.bot + 1
            return True
        elif self.bot > 12:
            return False



    def ayuda(self):

        pilas.almacenar_escena(escenas.escena_ayuda.iniciar(self.ls))



    def opciones(self):
        pilas.almacenar_escena(escenas.Opciones())

    def comenzar(self):
        if self.existe:
            pilas.cambiar_escena(escenas.escena_juego.iniciar(self.jugador,'existe'))
        else:
            pilas.cambiar_escena(escenas.escena_juego.iniciar(self.jugador,'newlevel'))

    def salir(self):
        import sys

        sys.exit(0)


iniciar = EscenaDeMenu
