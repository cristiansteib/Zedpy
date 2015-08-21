__author__ = 'sym'
# ultima actualizacion 17/06




class Punto(object):

    def setPunto(self,point):
      self._x = point[0]
      self._y = point[1]

    def getPunto(self):
        return(self._x,self._y)

    punto = property(getPunto, setPunto)


    def getX(self):
        return self._x


    def setX(self, x):
        self._x = x


    def getY(self):
         return self._y


    def setY(self, y):
        self._y = y

    x = property(getX, setX)

    y = property(getY, setY)


    def distancia(self,point):
        import math

        d = math.sqrt(((point[0] - self._x) ** 2) + ((point[1] - self._y) ** 2))
        return (d)

    def es_igual_a(self,point):
        if self._x == point[0] and self._y == point[1]:
            return True
        else:
            return False

#iniciar = Punto