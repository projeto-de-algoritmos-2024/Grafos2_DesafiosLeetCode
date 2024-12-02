class Solution:
    #Manipular heap
    def empurrar(self, heap, item):
        heap.append(item)
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

    def minimumWeight(self, n, edges, src1, src2, dest):
        from collections import defaultdict

        grafo = defaultdict(list)
        for u, v, w in edges:
            grafo[u].append((v, w))

        # Função Dijkstra a partir de src1
        def dijkstra(origem):
            distancias = [float('inf')] * n
            distancias[origem] = 0
            heap = []
            self.empurrar(heap, (0, origem))
            while heap:
                dist_atual, u = self.retirar(heap)
                if dist_atual > distancias[u]:
                    continue
                for v, peso in grafo[u]:
                    if distancias[v] > distancias[u] + peso:
                        distancias[v] = distancias[u] + peso
                        self.empurrar(heap, (distancias[v], v))
            return distancias

        dist_src1 = dijkstra(src1)

        # Verificar se dest é alcançável a partir de src1
        if dist_src1[dest] == float('inf'):
            return -1
        else:
            return dist_src1[dest]