class Problema(object):
    def __init__(self,estadoFinal):
        self.final = estadoFinal

    def verificaEstado(self,estado):
        if self.final == estado:
            return True
        return False

    def possibilidades(self,estado,mapa):
        opcoes = list(filter(lambda opt: opt[0] == estado, mapa))
        return opcoes