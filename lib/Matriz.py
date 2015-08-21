__author__ = 'cristian'
# -*- encoding: utf-8 -*-

"""
Este modulo permite crear un objeto matriz

"""

class Matriz():
    def __init__(self,numero_filas,numero_columnas):
        self.filas=numero_filas
        self.columnas=numero_columnas
        self.matriz = [None] * self.filas
        for i in range(0,self.filas):
            self.matriz[i] = [None] * self.columnas

    def printMatriz(self):
        for fila in range(0,self.filas):
            print self.matriz[fila]









    def set_valor(self,numero_de_fila,numero_de_columna,valor):
        self.matriz[numero_de_fila][numero_de_columna]=valor

    def get_valor (self,numero_de_fila,numero_de_columna):
        try:
              return self.matriz[numero_de_fila][numero_de_columna]
        except :
            print ('Matriz fuera del indice')
            return False


    def get_matriz (self):
        return self.matriz

    def get_transpuesta(self):
        self.matriz_transpuesta=self.__generar_transpuesta(self.matriz)
        return self.matriz_transpuesta




    def __generar_transpuesta(self,matriz):
        matriz_transpuesta = [None] * self.filas
        for i in range(0,self.filas):
            matriz_transpuesta[i] = [None] * self.columnas

        for f in range(0,self.filas):
            for c in range (0,self.columnas):
                matriz_transpuesta[f][c]=matriz[c][f]
        return matriz_transpuesta


