class Node(object):
    def __init__(self, estado, pai, custo, h):
        self.estado = estado
        self.pai = pai
        self.g = custo
        self.h = h
        self.f = self.g + self.h
    
    def __eq__(self,outro_node):
        return self.estado == outro_node.estado