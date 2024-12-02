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

    def minCost(self, maxTime, edges, passingFees):
        quantidadeCidades = len(passingFees)
        grafo = [[] for _ in range(quantidadeCidades)]
        for u, v, tempo in edges:
            grafo[u].append((v, tempo))
            grafo[v].append((u, tempo))

        minTempo = [float('inf')] * quantidadeCidades
        minTempo[0] = 0

        heap = []
        self.empurrar(heap, (passingFees[0], 0, 0))  # (custoTotal, tempoAtual, cidadeAtual)

        while heap:
            custoAtual, tempoAtual, cidadeAtual = self.retirar(heap)

            if tempoAtual > maxTime:
                continue

            if cidadeAtual == quantidadeCidades - 1:
                return custoAtual

            if tempoAtual > minTempo[cidadeAtual]:
                continue

            minTempo[cidadeAtual] = tempoAtual

            for vizinho, tempoAresta in grafo[cidadeAtual]:
                novoTempo = tempoAtual + tempoAresta
                novoCusto = custoAtual + passingFees[vizinho]

                if novoTempo <= maxTime and novoTempo < minTempo[vizinho]:
                    self.empurrar(heap, (novoCusto, novoTempo, vizinho))

        return -1