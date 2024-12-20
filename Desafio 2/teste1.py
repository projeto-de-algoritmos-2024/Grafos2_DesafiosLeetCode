#aplicar dijkstra para resolver esse problema com uma heap
#vou usar a manipulação de heap do exercicio anterior

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

#teste
if __name__ == "__main__":
    # Caso de teste 1
    maxTime1 = 30
    edges1 = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
    passingFees1 = [5,1,2,20,20,3]
    solution = Solution()
    resultado1 = solution.minCost(maxTime1, edges1, passingFees1)
    print("Custo mínimo para completar a jornada (Caso 1):", resultado1)  #11

    # Caso de teste 2
    maxTime2 = 29
    edges2 = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
    passingFees2 = [5,1,2,20,20,3]
    resultado2 = solution.minCost(maxTime2, edges2, passingFees2)
    print("Custo mínimo para completar a jornada (Caso 2):", resultado2)  #48

    # Caso de teste 3
    maxTime3 = 25
    edges3 = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
    passingFees3 = [5,1,2,20,20,3]
    resultado3 = solution.minCost(maxTime3, edges3, passingFees3)
    print("Custo mínimo para completar a jornada (Caso 3):", resultado3)  #-1