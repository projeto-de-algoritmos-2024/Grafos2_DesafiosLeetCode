# Enunciado

# [**2203. Subgrafo ponderado mínimo com os caminhos necessários**](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/)

Você recebe um inteiro `n`denotando o número de nós de um grafo **direcionado ponderado** . Os nós são numerados de `0`a `n - 1`.

Você também recebe uma matriz de inteiros 2D `edges`onde denota que existe uma aresta **direcionada** de para com peso .`edges[i] = [fromi, toi, weighti]fromitoiweighti`

Por fim, você recebe três inteiros **distintos**`src1` , `src2`, e `dest`denotando três nós distintos do gráfico.

Retorna *o **peso mínimo** de um subgrafo do grafo tal que seja **possível** alcançar* `dest` *de ambos* `src1` *e* `src2` *por meio de um conjunto de arestas deste subgrafo* . Caso tal subgrafo não exista, retorna `-1`.

Um **subgrafo** é um grafo cujos vértices e arestas são subconjuntos do grafo original. O **peso** de um subgrafo é a soma dos pesos de suas arestas constituintes.

**Exemplo 1:**

![https://assets.leetcode.com/uploads/2022/02/17/example1drawio.png](https://assets.leetcode.com/uploads/2022/02/17/example1drawio.png)

```
Entrada: n = 6, arestas = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
Saída: 9
Explicação:
A figura acima representa o gráfico de entrada.
As bordas azuis representam um dos subgráficos que produzem a resposta ideal.
Note que o subgrafo [[1,0,3],[0,5,6]] também produz a resposta ótima. Não é possível obter um subgrafo com menos peso satisfazendo todas as restrições.
```

**Exemplo 2:**

![https://assets.leetcode.com/uploads/2022/02/17/example2-1drawio.png](https://assets.leetcode.com/uploads/2022/02/17/example2-1drawio.png)

```
Entrada: n = 3, arestas = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
Saída: -1
Explicação:
A figura acima representa o gráfico de entrada.
Pode-se observar que não existe nenhum caminho do nó 1 ao nó 2, portanto não há subgráficos que satisfaçam todas as restrições.
```

**Restrições:**

- `3 <= n <= 105`
- `0 <= edges.length <= 105`
- `edges[i].length == 3`
- `0 <= fromi, toi, src1, src2, dest <= n - 1`
- `fromi != toi`
- `src1src2dest`
    
    ,
    
    , e
    
    são distintos aos pares.
    
- `1 <= weight[i] <= 105`