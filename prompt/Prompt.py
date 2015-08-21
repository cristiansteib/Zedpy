__author__ = 'cristian'

import lib
class Prompt(object):
    def __init__(self,filas=1,columnas=1):

        self.filas=filas
        self.columnas=columnas
        '''recibe filas y columnas para crear la matriz de posiciones del prompt'''
        self.__elementos=[]  #lista total de elementos del prompt
        self.elementos_visibles=[] #lista de elementos visibles en pantalla , es dependiente de mi variable dim_fisica
        self.coordinada_posiciones=lib.Matriz(filas,columnas)
        self.dim_fisica_visible=columnas
        self.dim_logica_visible=-1
        self.dim_logica=-1
        self.pos_cursor=0

        self.inicio=0
        self.fin=self.dim_fisica_visible

    def getElementos(self):
        '''retorna los elementos de la lista '''
        return self.__elementos




    def setElemento(self,elemento):
        self.__elementos.append(elemento)
        self.dim_logica=self.dim_logica+1
        r=self.manejador_elementos_visibles(elemento)
        return r

    elem = property(getElementos, setElemento)

    def getMatrizPosiciones(self):
        return self.coordinada_posiciones.get
    def getElementosVisibles(self):
        return self.elementos_visibles

    elemVisibles = property (getElementosVisibles)

    def get_dim_logica(self):
        '''retorna cantidad de elementos dentro de la lista . si es = -1 no contiene elementos'''
        return self.dim_logica

    def get_dim_logica_visible(self):
        return self.dim_logica_visible
    def get_dim_fisic_visible(self):
        return self.dim_fisica_visible
    def set_coordenadas(self,fila,columna,elemento):
        '''recibe tuplas, con punto (x,y) para la matriz de coordenadas
        requiere antes llamar a Prompt.set_cantidad_filas_columnas'''
        self.coordinada_posiciones.set_valor(fila,columna,elemento)

    def get_coordenada(self,fila,columna):
        if fila<self.filas and columna<self.columnas:
            return self.coordinada_posiciones.get_valor(fila,columna)
        else:
            return False




    def getPoscursor(self):
        '''retorna posicion actual del cursor '''
        return self.pos_cursor

    def setPoscursor(self,numero):
        self.pos_cursor=numero

    cursor = property(getPoscursor, setPoscursor)



    def inc_poscursor(self,cantidad=1):
        '''incrementa la possicion del cursor en cantidad,por default cantidad=1'''
        if self.pos_cursor<self.dim_fisica_visible:
            self.pos_cursor=self.pos_cursor+cantidad
            return True
        else:
            return False

    def dec_poscursor(self,cantidad=1):
        '''decrementa la possicion del cursor en cantidad,por default cantidad=1'''
        if (self.pos_cursor>0):
                self.pos_cursor=self.pos_cursor-cantidad
                return True
        else:
            return False

    def getElementoAnterior(self):
        return self.elem_anterior
    elemAnt = property (getElementoAnterior)

    def manejador_elementos_visibles(self,elemento):


        if self.dim_logica_visible<self.dim_fisica_visible-1:
            self.elementos_visibles.append(elemento)
            self.dim_logica_visible=self.dim_logica_visible+1



            return 'ok'

        if self.dim_logica_visible>self.dim_fisica_visible-2:

            self.elem_anterior=self.elementos_visibles[0]
            self.inicio=self.inicio+1
            self.fin=self.inicio+self.dim_fisica_visible
            self.elementos_visibles=self.__elementos[self.inicio:self.fin]

            return 'overflow'

    def desplaza_izquierda(self):
        '''si se puede desplazar a izquierda devuelve True , sino False'''
        if self.inicio>0:

            self.elem_anterior=self.elementos_visibles[self.dim_fisica_visible-1]
            self.inicio=self.inicio-1
            self.fin=self.inicio+self.dim_fisica_visible
            self.elementos_visibles=self.__elementos[self.inicio:self.fin]
            return True
        else:
            return False


    def desplaza_derecha(self):

        '''si se puede desplazar a izquierda devuelve True , sino False'''


        if self.fin<=self.dim_logica:
            self.elem_anterior=self.elementos_visibles[0]
            self.inicio=self.inicio+1
            self.fin=self.inicio+self.dim_fisica_visible
            self.elementos_visibles=self.__elementos[self.inicio:self.fin]
            return True
        else:
            return False

    def elimino_todo(self):
        self.elementos_visibles=[]
        self.__elementos=[]
        self.dim_logica_visible=-1
        self.dim_logica=-1
        self.inicio=0
        self.fin=self.dim_fisica_visible
        self.pos_cursor=0



iniciar=Prompt
