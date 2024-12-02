class Solution:
    # Funções auxiliares para manipular a heap
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

        # Construir o grafo
        grafo = defaultdict(list)
        grafo_invertido = defaultdict(list)
        for u, v, w in edges:
            grafo[u].append((v, w))
            grafo_invertido[v].append((u, w))

        def dijkstra(origem, grafo):
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

        dist_src1 = dijkstra(src1, grafo)
        dist_src2 = dijkstra(src2, grafo)
        dist_dest = dijkstra(dest, grafo_invertido)  # Grafo invertido para calcular distâncias até dest

        min_total = float('inf')
        for i in range(n):
            total = dist_src1[i] + dist_src2[i] + dist_dest[i]
            if total < min_total:
                min_total = total

        return min_total if min_total != float('inf') else -1

# Casos de teste
if __name__ == "__main__":
    # Caso de teste 1
    n = 6
    edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],
             [2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
    src1 = 0
    src2 = 1
    dest = 5
    solution = Solution()
    resultado = solution.minimumWeight(n, edges, src1, src2, dest)
    print("Peso mínimo total (Caso 1):", resultado)  #9

    # Caso de teste 2
    n2 = 3
    edges2 = [[0,1,1],[2,1,1]]
    src1_2 = 0
    src2_2 = 1
    dest_2 = 2
    resultado2 = solution.minimumWeight(n2, edges2, src1_2, src2_2, dest_2)
    print("Peso mínimo total (Caso 2):", resultado2)  #-1