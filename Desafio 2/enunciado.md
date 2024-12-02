[1928. Minimum Cost to Reach Destination in Times](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/description/?envType=problem-list-v2&envId=graph&difficulty=HARD)

Há um país de ncidades numeradas de 0a n - 1onde todas as cidades são conectadas por estradas bidirecionais. As estradas são representadas como uma matriz de inteiros 2D edgesonde denota uma estrada entre cidades e que leva minutos para viajar. Pode haver várias estradas com tempos de viagem diferentes conectando as mesmas duas cidades, mas nenhuma estrada conecta uma cidade a si mesma.edges[i] = [xi, yi, timei]xiyitimei

Cada vez que você passa por uma cidade, você deve pagar uma taxa de passagem. Isso é representado como um array inteiro indexado 0passingFees de comprimento nonde passingFees[j]é a quantia de dólares que você deve pagar quando passar por city j.

No começo, você está na cidade 0e quer chegar lá n - 1em maxTimeminutos ou menos . O custo da sua viagem é a soma das taxas de passagem para cada cidade pela qual você passou em algum momento da sua viagem ( incluindo as cidades de origem e destino).

Dado maxTime, edges, e passingFees, retorne o custo mínimo para concluir sua viagem, ou -1se você não puder concluí-la em maxTimeminutos .

Exemplo 1:

Entrada: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Saída: 11
Explicação: O caminho a seguir é 0 -> 1 -> 2 -> 5, que leva 30 minutos e tem US$ 11 em taxas de passagem.
Exemplo 2:

Entrada: maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Saída: 48
Explicação: O caminho a seguir é 0 -> 3 -> 4 -> 5, que leva 26 minutos e tem US$ 48 em taxas de passagem.
Você não pode seguir o caminho 0 -> 1 -> 2 -> 5, pois levaria muito tempo.
Exemplo 3:

Entrada: maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Saída: -1
Explicação: Não há como chegar à cidade 5 a partir da cidade 0 em 25 minutos.

Restrições:

1 <= maxTime <= 1000
n == passingFees.length
2 <= n <= 1000
n - 1 <= edges.length <= 1000
0 <= xi, yi <= n - 1
1 <= timei <= 1000
1 <= passingFees[j] <= 1000
O gráfico pode conter múltiplas arestas entre dois nós.
O gráfico não contém loops próprios.
