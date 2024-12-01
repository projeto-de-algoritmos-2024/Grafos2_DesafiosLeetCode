class Solution(object):
    def minCostConnectPoints(self, pontos):
        quantidadePontos = len(pontos)
        custoTotal = 0
        pontosVisitados = [False] * quantidadePontos
        custoMinimoParaConectar = [float('inf')] * quantidadePontos
        custoMinimoParaConectar[0] = 0 

        for _ in range(quantidadePontos):
            menorDistanciaAtual = float('inf')
            indiceProximoPonto = -1

            for i in range(quantidadePontos): # Selecionar o próximo ponto com menor custo
                if not pontosVisitados[i] and custoMinimoParaConectar[i] < menorDistanciaAtual:
                    menorDistanciaAtual = custoMinimoParaConectar[i]
                    indiceProximoPonto = i

            pontosVisitados[indiceProximoPonto] = True
            custoTotal += menorDistanciaAtual

            for j in range(quantidadePontos): # Atualiza os custos para conectar os outros pontos
                if not pontosVisitados[j]:
                    distanciaX = abs(pontos[indiceProximoPonto][0] - pontos[j][0])
                    distanciaY = abs(pontos[indiceProximoPonto][1] - pontos[j][1])
                    distanciaTotal = distanciaX + distanciaY
                    if distanciaTotal < custoMinimoParaConectar[j]:
                        custoMinimoParaConectar[j] = distanciaTotal
        return custoTotal

#teste
if __name__ == "__main__":
    solution = Solution()
    pontos = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    resultado = solution.minCostConnectPoints(pontos)
    print("O Mínimo para conectar todos os pontos:", resultado)  # Nesse caso de teste deve ser 20
