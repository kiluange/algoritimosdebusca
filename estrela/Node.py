class Node(object):
    def __init__(self, estado, pai, custo, h):
        self.estado = estado
        self.pai = pai
        self.custo = custo
        self.h = h
    
    def __eq__(self,outro_node):
        return self.estado == outro_node.estado