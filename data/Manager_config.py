# -*- encoding: utf-8 -*-
__author__ = 'cristian'

import json

"""
asas
"""


class Configuracion(object):
    def __init__(self):
        try:
            file = open("./data/config.json", "r")
            self.data = json.load(file)
            file.close()
            self.checkdic()
        except (IOError, EOFError, ImportError, KeyError, IndexError):
            file = open("./data/config.json", "w")
            self.data = self.default_values()
            json.dump(self.data, file, indent=4, separators=(',', ': '))
            file.close()
        except:
            print ('error inesperado,no se pudo crear/acceder al arhivo de configuracion')

    def checkdic(self):
        """chequea que esten todos las claves"""
        lista1 = ['robot', 'juego', 'modo_libre', 'graficos', 'sonidos']
        lista1.sort()
        listarobot = ['time', 'speed', 'name', 'id', 'board']
        listarobot.sort()
        listajuego = ['nivel', 'dificultad', 'movimientos_minimos', 'tiempo_max', 'tiempo_descuento',
                      'factormultiplicacionbombas', 'lvlup', 'cantidad_maxima_bombas', 'disminuir_puntos_bomba',
                      'factor_colision_vida','disminuir_puntos_tiempo']
        listajuego.sort()
        listamodolibre = ['time', 'speed']
        listamodolibre.sort()
        listagraficos = ['animacion']
        listagraficos.sort()
        listasonidos = ['volumen', 'sonido', 'musica']
        listasonidos.sort()

        try:
            lista1cmp = self.data.keys()
            lista1cmp.sort()
            listarobotcmp = self.data['robot'].keys()
            listarobotcmp.sort()
            listajuegocmp = self.data['juego'].keys()
            listajuegocmp.sort()
            listamodolibrecmp = self.data['modo_libre'].keys()
            listamodolibrecmp.sort()
            listagraficoscmp = self.data['graficos'].keys()
            listagraficoscmp.sort()
            listasonidoscmp = self.data['sonidos'].keys()
            listasonidoscmp.sort()

            if lista1 == lista1cmp and listarobot == listarobotcmp and listajuego == listajuegocmp and listamodolibre == listamodolibrecmp and listagraficos == listagraficoscmp and listasonidos == listasonidoscmp:
                print ('Configuracion: OK')
                return True
            else:
                print ('Configuracion: Mal')
                raise KeyError

        except (KeyError):
            print ('Estableciendo Configuracion por Default')
            file = open("./data/config.json", "w")
            self.data = self.default_values()
            json.dump(self.data, file, indent=4, separators=(',', ': '))
            file.close()

    def default_values(self):
        """
        setea por default los valores de todas las configuraciones

        """
        return {'robot': {'time': 2, 'speed': 50, 'name': 'multiplo_n6', 'id': 0, 'board': '/dev/ttyUSB0'},
                'juego': {'nivel': 0, 'dificultad': 0, 'movimientos_minimos': 15, 'tiempo_max': 15,
                          'tiempo_descuento': 20, 'factormultiplicacionbombas': 1.4, 'lvlup': False,
                          'cantidad_maxima_bombas': 100, 'disminuir_puntos_bomba': 250, 'factor_colision_vida': 1.2,
                          'disminuir_puntos_tiempo':300},
                'modo_libre': {'time': 2, 'speed': 50},
                'graficos': {'animacion': True},
                'sonidos': {'volumen': 100, 'sonido': True, 'musica': True}
                }

    def save_values(self):
        try:
            file = open("./data/config.json", "w")
            json.dump(self.data, file, indent=4, separators=(',', ': '))
            file.close()
            print ('Configuracion Salvada')
        except:
            print ('error inesperado,no se pudo guardar el arhivo de configuracion')

    ###########################################
    #####  ROBOT ##############################


    def getTimeRobot(self):
        return self.data['robot']['time']

    def setTimeRobot(self, value):
        self.data['robot']['time'] = value

    def getSpeedRobot(self):
        return self.data['robot']['speed']

    def setSpeedRobot(self, value):
        if value > 10 and value < 100:
            self.data['robot']['speed'] = value

    def getNameRobot(self):
        return self.data['robot']['name']

    def setNameRobot(self, value):
        self.data['robot']['name'] = value

    def getIdRobot(self):
        return self.data['robot']['id']

    def setIdRobot(self, value):
        if value > 255:
            value = 0
        self.data['robot']['id'] = value

    def getBoard(self):
        return self.data['robot']['board']

    def setBoard(self, value):
        self.data['robot']['board'] = value

    timerobot = property(fget=getTimeRobot, fset=setTimeRobot)
    speedrobot = property(fget=getSpeedRobot, fset=setSpeedRobot)
    namerobot = property(fget=getNameRobot, fset=setNameRobot)
    idrobot = property(fget=getIdRobot, fset=setIdRobot)
    board = property(getBoard, setBoard)


    ###########################################
    #####  JUEGO ##############################

    def getbombasmax(self):
        return self.data['juego']['cantidad_maxima_bombas']

    def setbombasmax(self, value):
        if value > 199:
            value = 200
        self.data['juego']['cantidad_maxima_bombas'] = value


    def getdisminuirpuntostiempo(self):
        return self.data['juego']['disminuir_puntos_tiempo']

    def setdisminuirpuntostiempo(self, value):
        self.data['juego']['disminuir_puntos_tiempo'] = value


    def getdisminuirpuntosbomba(self):
        return self.data['juego']['disminuir_puntos_bomba']

    def setdisminuirpuntosbomba(self, value):
        self.data['juego']['disminuir_puntos_bomba'] = value

    def getfactorcolisionvida(self):
        return self.data['juego']['factor_colision_vida']

    def setfactorcolisionvida(self, value):
        self.data['juego']['factor_colision_vida'] = value

    def getlvlup(self):
        return self.data['juego']['lvlup']

    def setlvlup(self, value):
        self.data['juego']['lvlup'] = value

    def getNivel(self):
        return self.data['juego']['nivel']

    def setNivel(self, value):
        self.data['juego']['nivel'] = value

    def getDificultad(self):
        return self.data['juego']['dificultad']

    def setDificultad(self, value):
        self.data['juego']['dificultad'] = value

    def getMovimientosMinimos(self):
        return self.data['juego']['movimientos_minimos']

    def setMovimientosMinimos(self, value):
        self.data['juego']['movimientos_minimos'] = value

    def getTiempoMaximo(self):
        return self.data['juego']['tiempo_max']

    def setTiempoMaximo(self, value):
        self.data['juego']['tiempo_max'] = value

    def getTiempoDescuento(self):
        return self.data['juego']['tiempo_descuento']

    def setTiempoDescuento(self, value):
        self.data['juego']['tiempo_descuento'] = value

    def getFMB(self):
        return self.data['juego']['factormultiplicacionbombas']

    def setFMB(self, value):
        self.data['juego']['factormultiplicacionbombas'] = value

    nivel = property(getNivel, setNivel)
    dificultad = property(getDificultad, setDificultad)
    movimientosminimos = property(getMovimientosMinimos, setMovimientosMinimos)
    tiempomaximo = property(getTiempoMaximo, setTiempoMaximo)
    tiempodescuento = property(getTiempoDescuento, setTiempoDescuento)
    fmb = property(getFMB, setFMB)
    lvlup = property(getlvlup, setlvlup)
    bombasmax = property(getbombasmax, setbombasmax)
    disminuirptosbomba = property(getdisminuirpuntosbomba, setdisminuirpuntosbomba)
    disminuirptostiempo= property(getdisminuirpuntostiempo,setdisminuirpuntostiempo)
    factcolision = property(getfactorcolisionvida,setfactorcolisionvida)

    ##################################################
    #######MODO LIBRE###########################


    def getTimeRobotVirtual(self):
        return self.data['modo_libre']['time']

    def setTimeRobotVirtual(self, value):
        self.data['modo_libre']['time'] = value

    def getSpeedRobotVirtual(self):
        return self.data['modo_libre']['speed']

    def setSpeedRobotVirtual(self, value):
        self.data['modo_libre']['speed'] = value

    timevirtual = property(getTimeRobotVirtual, setTimeRobotVirtual)
    speedvirtual = property(getSpeedRobotVirtual, setSpeedRobotVirtual)

    ##############################################
    ######### Graficos############################

    def getAnimacion(self):
        return self.data['graficos']['animacion']

    def setAnimacion(self, value):
        self.data['graficos']['animacion'] = value

    graficos = property(getAnimacion, setAnimacion)

    #############################################
    ###########SONIDOS##########################

    def getVolumen(self):
        return self.data['sonidos']['volumen']

    def setVolumen(self, value):
        self.data['sonidos']['volumen'] = value

    def getSonido(self):
        return self.data['sonidos']['sonido']

    def setSonido(self, value):
        self.data['sonidos']['sonido'] = value

    def getMusica(self):
        return self.data['sonidos']['musica']

    def setMusica(self, value):
        self.data['sonidos']['musica'] = value

    volumen = property(getVolumen, setVolumen)
    sonido = property(getSonido, setSonido)
    musica = property(getMusica, setMusica)
