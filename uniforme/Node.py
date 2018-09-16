from Problema import Problema
class Node(object):
    def __init__(self,estadoAtual,problema,node,custo):
        self.estadoAtual = estadoAtual
        self.problema = problema
        self.node = node
        self.custo = custo

    def __eq__(self,outro_node):
        return self.estadoAtual is outro_node.estadoAtual