__author__ = 'cristian'
__doc__ = """
    Este modulo transforma los movimientos enviado de la forma ('movimiento',cantidad)
    a una ubicacion dentro del mapa.
    movimiento= 'avanzar',

    El personaje puede tener 4 posiciones a las que apunta para avanzar o retroceder
    0=Apunta ARRIBA
    1=Apunta DERECHA
    2=Apunta ABAJO
    3=Apunta IZQUIERDA
"""


class Transformador:
    def __init__(self,cant_filas,cant_columnas,posicion_inicial,apunta_actor=0):
         #recibe posicion inicial (fila,columna) que es dentro de mapa
        self.posicion_inicial=posicion_inicial
        self.apunta_actor=apunta_actor
        self.apunta_actor_inicial=apunta_actor
        self.pos_recorrido={}
        self.filas=cant_filas
        self.columnas=cant_columnas
        self.habilitado=True

    def set_Movimientos(self,diccionario):
        #recibe el diccionario y lo transforma
        self.apunta_actor=self.apunta_actor_inicial
        self.__convertidor(diccionario)


    def get_Movimientos(self):
        return self.pos_recorrido

    def getApunta_actor(self):
        #devuelve la posicion hacia donde estaba apuntando
        return self.apunta_actor

    def __convertidor(self,diccionario_movimientos):

        lista_claves=diccionario_movimientos.keys()
        i=0
        pos_ant=self.posicion_inicial
        pos_act=self.posicion_inicial
        for clave in lista_claves:
            movimiento=diccionario_movimientos[clave]
            if movimiento[1]==0:
                veces=1
            elif movimiento[1]>0:
                veces=movimiento[1]

            if movimiento[0]=='avanzar' and self.habilitado:
                if self.apunta_actor==0:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0]+1,pos_ant[1],self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[0]<self.filas:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

                if self.apunta_actor==1 and self.habilitado:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0],pos_ant[1]+1,self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[1]<self.columnas:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

                if self.apunta_actor==2 and self.habilitado:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0]-1,pos_ant[1],self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[0]>=0:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

                if self.apunta_actor==3 and self.habilitado:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0],pos_ant[1]-1,self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[1]>=0:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1


            if movimiento[0]=='retroceder' and self.habilitado:
                if self.apunta_actor==0:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0]-1,pos_ant[1],self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[0]>=0:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

                if self.apunta_actor==1 and self.habilitado:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0],pos_ant[1]-1,self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[1]>=0:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

                if self.apunta_actor==2 and self.habilitado:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0]+1,pos_ant[1],self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[0]<self.filas:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

                if self.apunta_actor==3 and self.habilitado:
                    for x in range (0,veces):
                        pos_act=(pos_ant[0],pos_ant[1]+1,self.apunta_actor)
                        pos_ant=pos_act
                        if pos_act[1]<self.columnas:
                            self.pos_recorrido[i]=pos_act
                            i=i+1
                        else:
                            self.pos_recorrido[i]=False
                            self.habilitado=False
                            i=i+1

            if movimiento[0]=='der':
                self.apunta_actor=self.apunta_actor+veces
                self.apunta_actor=self.apunta_actor%4


            if movimiento[0]=='izq':
                self.apunta_actor=self.apunta_actor-veces
                self.apunta_actor=self.apunta_actor%4

iniciar=Transformador