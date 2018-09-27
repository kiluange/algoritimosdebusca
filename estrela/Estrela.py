from Node import Node
from Problema import Problema
import copy

class Estrela(object):

    explorados = []
    fronteira = []

    def __init__(self, *args):
        self.problema = Problema(args[1])
        self.fronteira = []
        pai = Node(args[0],None,0,self.h(args[0]))
        self.fronteira.append(pai)
        self.busca()
        pass
    
    def g(self):
        pass

    def h(self,estado):
        xAxis1 = None
        yAxis1 = None

        xAxis2 = None
        yAxis2 = None

        D = 0

        for i in range(1,9):
            for e in estado:
                if i in e:
                    xAxis1 = estado.index(e)
                    yAxis1 = e.index(i)
            for o in self.problema.objetivo:
                if i in o:
                    xAxis2 = self.problema.objetivo.index(o)
                    yAxis2 = o.index(i)
            D += abs(xAxis1 - xAxis2) + abs(yAxis1 - yAxis2)

        return D
    
    def verifica(self,pai):
        if pai.estado == self.problema.objetivo:
            return True

    def busca(self):

        if (len(self.fronteira) is 0):
            return False

        pai = self.fronteira.pop(0)
        print('pai ' + str(pai.estado)+ ' g = ' + str(pai.g) + ' h = ' + str(pai.h))

        if self.verifica(pai):
            print(str(pai.estado)+' g = '+str(pai.g))
            return pai

        self.explorados.append(pai)
        for m in self.problema.movimentos(pai.estado):
            filho = Node(m,pai,pai.g + 1, self.h(m))
            print(str(filho.estado)+" g = "+str(filho.g)+" h = "+str(filho.h))
            if filho not in self.fronteira and filho not in self.explorados:
                self.fronteira.append(filho)
            else:
                for f in self.fronteira:
                    if filho.estado == f.estado and filho.f < f.f:
                        f = copy.deepcopy(filho)
            self.fronteira.sort(key=lambda x: x.f)
        self.busca()

Estrela([[4,2,3],[1,0,8],[7,5,6]],[[1,2,3],[4,5,6],[7,8,0]])