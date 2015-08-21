__author__ = 'cristian'
class Movimientos:
    def  __init__(self):
        self.diccionario_real={}
        self.diccionario_aux={}
        self.indice=0

    def add_Movimiento(self,valor):
        self.diccionario_real[self.indice]=valor
        self.indice=self.indice+1

    def get_Movimientos(self):
        return self.diccionario_real

    def get_Movimiento(self,key):
        if self.diccionario_real.has_key(key):
            return self.diccionario_real[key]
        else:
            return False

    def get_Indice_movimientos(self):
        return self.indice

    def elimiarMovimiento(self,key):
        if self.diccionario_real.has_key(key):
            self.diccionario_real.pop(key)
            lista_key=self.diccionario_real.keys()
            self.indice=0
            for key in lista_key :
                self.diccionario_aux[self.indice] = self.diccionario_real[key]
                self.indice=self.indice+1
            self.diccionario_real=self.diccionario_aux
            return True
        else:
            return False

    def elimiarmovimientopop(self):
        if self.diccionario_real.has_key(self.indice-1):
            self.diccionario_real.pop(self.indice-1)
            self.indice-=1




iniciar=Movimientos