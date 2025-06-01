# quicksort-complexidade

# Análise de Complexidade: Quick Sort

Trabalho da disciplina **Teoria da Computação** (Professores Pâmela e Daniel)

## 👨‍💻 Integrantes
- Luca Santos
- Luca Souto
- Rodrigo Nunes

## 📌 Algoritmo
Quick Sort

## 🛠 Linguagens utilizadas
- Python
- Java

## 📖 Descrição do Algoritmo
O Quick Sort é um algoritmo de ordenação eficiente baseado na estratégia de divisão e conquista. Ele seleciona um elemento como pivô e particiona o array em dois subarrays, colocando elementos menores à esquerda e maiores à direita do pivô, e então ordena recursivamente os subarrays.

### Pseudocódigo
```plaintext
QUICKSORT(A, baixo, alto)
    se baixo < alto
        pivo ← PARTITION(A, baixo, alto)
        QUICKSORT(A, baixo, pivo-1)
        QUICKSORT(A, pivo+1, alto)
```

## 📊 Classificação Assintótica
- **Melhor caso:** O(n log n)
- **Caso médio:** O(n log n)
- **Pior caso:** O(n²)
- **Notação:** O(n log n), Ω(n log n), Θ(n log n) (na média)

## 💡 Aplicabilidade Prática
Quick Sort é eficiente para grandes volumes de dados e é amplamente utilizado em bibliotecas padrão. Não é estável, mas é in-place e geralmente mais rápido que outros algoritmos de ordenação em aplicações práticas.

## 📈 Conteúdo
- Implementações do algoritmo em Python e Java
- Scripts para geração de entrada e medição de tempo
- Gráficos e análise comparativa
- Relatório final em PDF

## 📊 Resultados
Os experimentos foram realizados com entradas de tamanhos 100, 10.000 e 1.000.000 com 30 execuções por teste. A média e o desvio padrão dos tempos de execução foram analisados e comparados entre as linguagens.

## 📂 Organização
Veja a estrutura de diretórios para acessar os arquivos relevantes.

## ▶️ Como Executar

### 1. Ativando o ambiente virtual Python

No terminal, dentro da raiz do projeto:

No Windows (Prompt de Comando):
```
.venv\Scripts\activate
```
No Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```

### 2. Instalando as dependências

Com o ambiente virtual ativado, instale o matplotlib:
```
pip install matplotlib
```

### 3. Gerando arquivos de entrada

Execute o gerador de entradas:
```
python input_generator/generate_input.py
```
Os arquivos `entrada_100.txt`, `entrada_10000.txt` e `entrada_1000000.txt` serão criados na raiz do projeto.

### 4. Executando o Quick Sort em Python

Execute o script de medição de tempo:
```
python python/quicksort_tempo.py
```
Os tempos médios e desvios serão exibidos no terminal.

### 5. Executando o Quick Sort em Java

Compile e execute o código Java:
```
cd java
javac QuickSortTimer.java
java QuickSortTimer
```
Os resultados serão exibidos no terminal.

### 6. Gerando o gráfico de comparação

Execute o script para gerar o gráfico:
```
python python/grafico_tempo.py
```
O arquivo `tempo_execucao.png` será salvo na raiz do projeto.

### 7. Desativando o ambiente virtual

Quando terminar, desative o ambiente virtual:
```
deactivate
```

## 📎 Relatório
Veja o [Relatório Final](Relatorio_QuickSort_Entrega2.pdf), que contém:
- Explicação teórica detalhada
- Análise de complexidade (melhor, pior, média)
- Discussão sobre aplicabilidade e reflexões finais (classe P, NP, etc)
- Resultados práticos, gráficos e tabelas
- Código-fonte dos algoritmos e scripts

## 🧠 Reflexão Final
O Quick Sort pertence à classe P, pois pode ser resolvido em tempo polinomial. Não há versão NP do problema de ordenação, mas problemas de ordenação parcial podem estar relacionados a problemas NP-completos em outros contextos.

## 📁 Código-fonte
Todo o código-fonte está disponível neste repositório, incluindo implementações, scripts de geração de entrada, análise de tempo e geração de gráficos.
