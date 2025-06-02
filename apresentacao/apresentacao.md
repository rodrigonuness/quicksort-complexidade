# Apresentação: Análise de Complexidade - Quick Sort

## Slide 1: Introdução
- **Disciplina:** Teoria da Computação
- **Professores:** Pâmela e Daniel
- **Integrantes:** Lucas Santos, Lucas Souto, Rodrigo Nunes
- **Algoritmo:** Quick Sort
- **Linguagens:** Python e Java
- **Repositório:** [GitHub](https://github.com/rodrigonuness/quicksort-complexidade)

### Falas:
"Bom dia! Hoje vamos apresentar nosso trabalho sobre o algoritmo Quick Sort, desenvolvido para a disciplina de Teoria da Computação. O grupo é composto por Lucas Santos, Lucas Souto e Rodrigo Nunes. Utilizamos Python e Java para implementar o algoritmo, e o código está disponível no GitHub."

---

## Slide 2: Descrição do Algoritmo
- **Estratégia:** Divisão e conquista
- **Funcionamento:**
  - Escolhe um elemento como pivô
  - Particiona a lista em dois subconjuntos:
    - Menores que o pivô
    - Maiores que o pivô
  - Ordena recursivamente os subconjuntos
- **Pseudocódigo:**
```plaintext
QUICKSORT(A, baixo, alto)
    se baixo < alto
        pivo ← PARTITION(A, baixo, alto)
        QUICKSORT(A, baixo, pivo-1)
        QUICKSORT(A, pivo+1, alto)
```

### Falas:
"O Quick Sort é um algoritmo de ordenação baseado na estratégia de divisão e conquista. Ele escolhe um elemento como pivô, particiona a lista em dois subconjuntos e aplica recursivamente o mesmo processo até que a lista esteja ordenada. Aqui está o pseudocódigo que representa o funcionamento básico do algoritmo."

---

## Slide 3: Escolha do Pivô
- **Python:** Pivô é o elemento central da lista
  - Melhor desempenho em listas parcialmente ordenadas
- **Java:** Pivô é o último elemento da lista
  - Simples de implementar, mas pode levar ao pior caso em listas ordenadas ou inversamente ordenadas

### Falas:
"Uma parte importante do Quick Sort é a escolha do pivô. Na implementação em Python, utilizamos o elemento central da lista, o que pode oferecer um desempenho mais estável em listas parcialmente ordenadas. Já na implementação em Java, optamos pelo último elemento como pivô, uma abordagem mais simples, mas que pode levar ao pior caso de desempenho em listas já ordenadas ou inversamente ordenadas."

---

## Slide 4: Resultados Experimentais
- **Entradas:** 100, 10.000, 1.000.000 elementos
- **Execuções:** 30 por teste
- **Tempos Médios e Desvios Padrão:**
| Tamanho da Entrada (n) | Python - Tempo Médio (s) | Python - Desvio Padrão (s) | Java - Tempo Médio (s) | Java - Desvio Padrão (s) |
|-------------------------|--------------------------|----------------------------|-------------------------|--------------------------|
| 100                     | 0.0003                  | 0.00005                    | 0.0001                 | 0.00002                  |
| 10.000                  | 0.025                   | 0.002                      | 0.012                  | 0.001                    |
| 1.000.000               | 2.3                     | 0.12                       | 1.2                    | 0.08                     |

### Falas:
"Realizamos experimentos com entradas de tamanhos 100, 10.000 e 1.000.000 elementos, executando cada teste 30 vezes. Aqui estão os tempos médios e desvios padrão obtidos para Python e Java. Como esperado, o desempenho do Java foi mais rápido, especialmente para entradas maiores, devido à implementação in-place."

---

## Slide 5: Discussão e Aplicabilidade
- **Complexidade:**
  - Melhor caso: O(n log n)
  - Caso médio: Θ(n log n)
  - Pior caso: O(n²)
- **Aplicabilidade:**
  - Ampla utilização em grandes volumes de dados
  - Python: Não é in-place, maior uso de memória
  - Java: In-place, mais eficiente em memória
- **Otimizações possíveis:**
  - Escolha de pivô aleatório ou mediana para evitar o pior caso

### Falas:
"Em termos de complexidade, o Quick Sort apresenta O(n log n) no melhor e caso médio, mas pode atingir O(n²) no pior caso, dependendo da escolha do pivô. Apesar disso, é amplamente utilizado devido à sua eficiência prática. A implementação em Python não é in-place, o que aumenta o uso de memória, enquanto a versão em Java é mais eficiente nesse aspecto. Estratégias como pivôs aleatórios ou medianas podem ajudar a evitar o pior caso."

---

## Slide 6: Conclusão
- **Reflexão Final:**
  - Quick Sort pertence à classe P (tempo polinomial)
  - É eficiente na prática, mas pode ser otimizado
- **Resultados:**
  - Python e Java apresentaram tempos consistentes com a teoria
  - Gráficos e tabelas mostram a relação entre tamanho da entrada e desempenho
- **Próximos passos:**
  - Explorar outras estratégias de escolha de pivô
  - Comparar com outros algoritmos de ordenação

### Falas:
"Para concluir, o Quick Sort pertence à classe P, sendo resolvido em tempo polinomial. Ele é eficiente na prática, mas pode ser otimizado com escolhas melhores de pivô. Os resultados obtidos foram consistentes com a teoria, e os gráficos e tabelas mostram claramente a relação entre o tamanho da entrada e o desempenho. Como próximos passos, podemos explorar outras estratégias de escolha de pivô e comparar o Quick Sort com outros algoritmos de ordenação."

