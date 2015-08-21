# -*- encoding: utf-8 -*-
# Robot-Game a game of robot
#
#
#
#
#

import pickle

__author__ = 'sym'
__doc__ = """
    Modulo Manager:
    ============
    Probado en Windows 8.1/Linux Ubuntu 15.04

    Este modulo es el encargado de manejar los archivos con los datos de los jugadores
    donde cada jugador tiene si respectivos datos .
    El archivo por dentro tiene la siguiente estructura:
     DATOS = {'nombre_de_jugador':{'edad':int_edad,niveles:{1:(vidas_perdidas,vidas_ganadas,puntaje,puntaje_maximo,tiempo_en ese nivel)}}, 'siguiente_jugador':{{}}}

    Otra representacion de forma jerarquica:

            DATOS:
                +nombre_de_jugador:        ||>>>PRIMER CLAVE DEL DICCIONARIO DE DATOS
                        -edad:                  ||>>>'edad'    CLAVE DENTRO DEL DICCIONARIO JUGADORES
                        +niveles:               ||>>>'niveles'  CLAVE DENTRO DEL DICCIONARIO JUGADORES
                               +numero_de_nivel:          ||>>>'numero_de_nivel' CLAVES DENTRO DEL DICCIONARIO NIVELES
                                    -vidas_perdidas                                                 ||
                                    -vida total  //numero de vida al iniciar el nivel               ||
                                    -puntaje_alcanzado                                              ||>>>>> TUPLA QUE CONTIENE ESTOS DATOS
                                    -puntaje_maximo                                                 ||
                                    -tiempo_en_ese_nivel                                            ||


    ej:
        valor= datos[nombre_de_jugador][nivel][0]
        valor quedaria con el valor de vidas_perdidas en el nivel=int , para el nombre_de_jugador='string'


"""


class Manager(object):
    def __init__(self):
        """

        :type self: object
        """
        self._datos = {}
        self._names = []
        self._actualizar_diccionario()

    def _actualizar_diccionario(self):
        try:
            data = open("./data/data_file.sym", "rb")
            # self.datos ES EL DICCIONARIO QUE CONTIENE TODOS LOS DATOS DESCRIPTOS EN EL __doc__
            self._datos = pickle.load(data)
            self._names = self._datos.keys()

            data.close()
        except (IOError, EOFError, ImportError, KeyError, IndexError):
            print ('se crea el archivo')
            data = open("./data/data_file.sym", "wb")
            data.close()
        except:
            print ('error inesperado,no se pudo crear/acceder al arhivo de datos')

    def guardar_jugador(self, jugador='nombre', datos={}):
        # GUARDA TODOS LO DATOS DEL JUGADOR DENTRO DEL ARCHIVO DE DATOS
        # ESTE METODO SOBRESCRIBE ,O CREA EL NUEVO JUGADOR. LA LOGICA DEL PROGRAMA
        # SERA LA ENCARGADA DE TENER EL CRITERIO SOBRE COMO MANEJA EL JUGADOR
        try:
            data = open("./data/data_file.sym", "wb")
            self._datos[jugador] = datos
            self._names = self._datos.keys()  # actualizo la lista de los nombres de jugadores
            pickle.dump(self._datos, data)
            data.close()
            print ('Jugador guardado exitosamente')
            return True
        except():
            print ('Error inesperado,no se pudo guardar')
            return False

    def getJugadores(self):
        # Devuelve una lista con todos los nombres de los jugadores
        return self._names

    def checkusuario(self, nombre):
        # si el usuario no existe devuelve False
        # caso contrario si existe un True
        if self._names.count(nombre) == 0:
            print 'no existe el usuario : %s ' % nombre
            return False
        else:
            return True

    def getJugador(self, name):
        # Devuelve solos los datos del jugador solicitado
        try:
            return self._datos[name]
        except(KeyError):
            print 'no se encuentra {0}'.format(name)
            return 'None'
