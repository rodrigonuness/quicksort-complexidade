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
Veja o [Relatório Final](Relatorio_QuickSort_Entrega2.pdf)
