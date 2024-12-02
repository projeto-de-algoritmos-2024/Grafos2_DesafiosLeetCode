[1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=problem-list-v2&envId=graph&difficulty=MEDIUM)

Você recebe uma matriz `points`representando coordenadas inteiras de alguns pontos em um plano 2D, onde .`points[i] = [xi, yi]`

O custo de conectar dois pontos e é a **distância de Manhattan** entre eles: , onde denota o valor absoluto de .`[xi, yi][xj, yj]|xi - xj| + |yi - yj||val|val`

Retorna *o custo mínimo para fazer todos os pontos conectados.* Todos os pontos são conectados se houver **exatamente um** caminho simples entre quaisquer dois pontos.

**Exemplo 1:**

!https://assets.leetcode.com/uploads/2020/08/26/d.png

```
Entrada: pontos = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Saída: 20
Explicação:
Podemos conectar os pontos como mostrado acima para obter o custo mínimo de 20.
Observe que há um caminho único entre cada par de pontos.
```

!https://assets.leetcode.com/uploads/2020/08/26/c.png

**Exemplo 2:**

```
Entrada: pontos = [[3,12],[-2,5],[-4,1]]
Saída: 18

```

**Restrições:**

- `1 <= points.length <= 1000`
- `106 <= xi, yi <= 106`
- Todos os pares são distintos.`(xi, yi)`
