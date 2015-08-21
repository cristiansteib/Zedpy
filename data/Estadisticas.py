__author__ = 'GasparcitoX'

'''
   los datos dentro del nivel son una tupla ordenada de enteros con los siguientes elementos:

    0    {  'vidas_lost'         : 2,
    1       'vidas_start'        : 3,
    2       'pto_max'            :1000,
    3       'pto_obtenido'       :300,
    4       'tiempo_total'       :20,
    5       'tiempo_minimo'      :30,
    6       'movimientos_minimos' :12,
    7       'movimientos_hechos' :12,
    8       'cantidad_choques'   :2,
    9       'cantidad_caidas'    :23  }

'''


import data

class Estadisticas():
    '''
        Devuelve un diccionario con la informacion de las estadisticas del jugador
    '''


    def get_individual(self,nombre):
        self.eficacia_total = 0
        self.tiempo_total = 0
        self.puntos_total = 0
        self.dic={}
        #jugador = data.Jugador()
        #jugador.nombre = nombre
        l_niveles =[0,1,2,3]# jugador.niveles           #obtengo la lista de niveles del jugador nombre
        for x in l_niveles :
            #jugador.niveldatos = x
            datos = {'vidas_end':6,'vidas_start':5,'pto_obtenido':1000,'pto_max':1000,'tiempo_minimo':5,'tiempo_total':5,'movimientos_minimos':30,'movimientos_hechos':30,'cantidad_choques':0,'cantidad_caidas':0}  #jugador.niveldatos
            ef_vida = (datos['vidas_end'] * 100) / datos['vidas_start'] if datos['vidas_end'] <=  datos['vidas_start'] else 100
            ef_puntos = (datos['pto_obtenido'] * 100) / datos['pto_max']
            ef_tiempo = (datos['tiempo_minimo'] * 100) / datos['tiempo_total']
            ef_mov = (datos['movimientos_minimos'] * 100) / datos['movimientos_hechos']
            #print ('{0:2}{1:5}{2:10}{3:15}').format(ef_vida,ef_puntos,ef_tiempo,ef_mov)
            eficacia_parcial = (ef_vida + ef_puntos + ef_tiempo + ef_mov) / 4
            self.tiempo_total = self.tiempo_total + datos['tiempo_total']
            self.puntos_total = self.puntos_total + datos['pto_obtenido']
            self.eficacia_total = self.eficacia_total + eficacia_parcial
            self.dic[x] = (eficacia_parcial,datos['tiempo_total'],datos['pto_obtenido'],datos['cantidad_choques'],datos['cantidad_caidas'])

        return (self.dic)

    def get_total(self,nombre):
        #jugador = data.Jugador()
        l_jugadores = ['jorge','pedro','juan']#jugador.jugadores   #obtengo la lista de nombres

        for x in l_jugadores :
            dic_total = get_individual(nombre)
            dic_total['total']=(self.eficacia_total,self.tiempo_total,self.puntos_total,datos['cantidad_choques'],datos['cantidad_caidas'])
        return (dic_total)





