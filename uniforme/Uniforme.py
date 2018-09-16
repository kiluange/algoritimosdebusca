from Node import Node
from Problema import Problema
import csv
import time
import sys

class Agente(object):

    explorados = []
    fronteira = []
    mapa = []

    def __init__(self,*args):
        node = Node(args[0],Problema(args[1]),None,0)
        self.opencsv(args[2])
        self.fronteira.append(node)
        self.busca()        

    def opencsv(self,mapaCsv):
        with open(mapaCsv, 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                self.mapa.append([row['current'],row['goal'],int(row['distance'])])

    def busca(self):

        if (len(self.fronteira) is 0):
            return False

        parent = self.fronteira.pop(0)

        if parent.problema.verificaEstado(parent.estadoAtual):
            print('em ' + str(parent.estadoAtual) + ' com custo ' + str(parent.custo))
            return True    

        self.explorados.append(parent)

        for possibilidade in parent.problema.possibilidades(parent.estadoAtual,self.mapa):
            child = Node(possibilidade[1],parent.problema,parent,parent.custo + int(possibilidade[2]))
            if child not in self.fronteira and child not in self.explorados:
                self.fronteira.append(child)
            else:
                for f in self.fronteira:
                    if child.estadoAtual == f.estadoAtual and child.custo < f.custo:
                        f = child
        self.fronteira.sort(key=lambda x: x.custo)
        self.busca()
inicio = time.time()
Agente(sys.argv[1],sys.argv[2],sys.argv[3])
fim = time.time()
print('run time ' + str(fim - inicio) + " seconds")