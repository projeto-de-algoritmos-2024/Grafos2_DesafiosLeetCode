class Solution(object):
    # manipular a heap
    def empurrar(self, heap, elemento):
        heap.append(elemento)
        self.subirElemento(heap, len(heap) - 1)

    def retirar(self, heap):
        if len(heap) == 1:
            return heap.pop()
        menor = heap[0]
        heap[0] = heap.pop()
        self.descerElemento(heap, 0)
        return menor

    def subirElemento(self, heap, indice):
        pai = (indice - 1) // 2
        while indice > 0 and heap[indice][0] < heap[pai][0]:
            heap[indice], heap[pai] = heap[pai], heap[indice]
            indice = pai
            pai = (indice - 1) // 2

    def descerElemento(self, heap, indice):
        menor = indice
        esquerda = 2 * indice + 1
        direita = 2 * indice + 2

        if esquerda < len(heap) and heap[esquerda][0] < heap[menor][0]:
            menor = esquerda
        if direita < len(heap) and heap[direita][0] < heap[menor][0]:
            menor = direita

        if menor != indice:
            heap[indice], heap[menor] = heap[menor], heap[indice]
            self.descerElemento(heap, menor)

    def minCostConnectPoints(self, pontos):
        quantidadePontos = len(pontos)
        custoTotal = 0
        pontosVisitados = [False] * quantidadePontos
        heap = []

        self.empurrar(heap, (0, 0))  # (custo, índice do ponto)

        while heap:
            custoAtual, pontoAtual = self.retirar(heap)
            if pontosVisitados[pontoAtual]:
                continue

            pontosVisitados[pontoAtual] = True
            custoTotal += custoAtual

            
            for proximoPonto in range(quantidadePontos): # Atualiza a heap com os custos para os pontos não visitados
                if not pontosVisitados[proximoPonto]:
                    distanciaX = abs(pontos[pontoAtual][0] - pontos[proximoPonto][0])
                    distanciaY = abs(pontos[pontoAtual][1] - pontos[proximoPonto][1])
                    distanciaTotal = distanciaX + distanciaY
                    self.empurrar(heap, (distanciaTotal, proximoPonto))

        return custoTotal
