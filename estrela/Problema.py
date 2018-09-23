import copy

class Problema(object):
    def __init__(self,objetivo):
        self.objetivo = objetivo
    
    def movimentos(self,estado):
        xAxis = None
        yAxis = None

        for x in estado:
            if 0 in x:
                xAxis = estado.index(x)
                yAxis = x.index(0)
        
        if   xAxis == 0 and yAxis == 0:
            return [self.direita(copy.deepcopy(estado),xAxis,yAxis),self.baixo(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 1 and yAxis == 0:
            return [self.cima(copy.deepcopy(estado),xAxis,yAxis),self.direita(copy.deepcopy(estado),xAxis,yAxis),self.baixo(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 2 and yAxis == 0:
            return [self.cima(copy.deepcopy(estado),xAxis,yAxis),self.direita(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 0 and yAxis == 1:
            return [self.esquerda(copy.deepcopy(estado),xAxis,yAxis),self.direita(copy.deepcopy(estado),xAxis,yAxis),self.baixo(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 1 and yAxis == 1:
            return [self.esquerda(copy.deepcopy(estado),xAxis,yAxis),self.cima(copy.deepcopy(estado),xAxis,yAxis),self.direita(copy.deepcopy(estado),xAxis,yAxis),self.baixo(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 2 and yAxis == 1:
            return [self.esquerda(copy.deepcopy(estado),xAxis,yAxis),self.cima(copy.deepcopy(estado),xAxis,yAxis),self.direita(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 0 and yAxis == 2:
            return [self.esquerda(copy.deepcopy(estado),xAxis,yAxis),self.baixo(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 1 and yAxis == 2:
            return [self.esquerda(copy.deepcopy(estado),xAxis,yAxis),self.cima(copy.deepcopy(estado),xAxis,yAxis),self.baixo(copy.deepcopy(estado),xAxis,yAxis)]
        elif xAxis == 2 and yAxis == 2:
            return [self.esquerda(copy.deepcopy(estado),xAxis,yAxis),self.cima(copy.deepcopy(estado),xAxis,yAxis)]
    
    
    def esquerda(self,est,xAxis,yAxis):
        temp = est[xAxis][yAxis - 1]
        esq = est
        esq[xAxis][yAxis - 1] = 0
        esq[xAxis][yAxis] = temp
        return (esq)
 
    def cima(self,est,xAxis,yAxis):
        temp = est[xAxis - 1 ][yAxis]
        cim = est
        cim[xAxis - 1][yAxis] = 0
        cim[xAxis][yAxis] = temp
        return(cim)
    
    def direita(self,est,xAxis,yAxis):
        temp = est[xAxis][yAxis + 1]
        dire = est
        dire[xAxis][yAxis + 1] = 0
        dire[xAxis][yAxis] = temp
        return dire
    
    def baixo(self,est,xAxis,yAxis):
        temp = est[xAxis + 1 ][yAxis]
        bai = est
        bai[xAxis + 1][yAxis] = 0
        bai[xAxis][yAxis] = temp
        return bai