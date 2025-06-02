import matplotlib.pyplot as plt
import numpy as np

# Dados reais obtidos do arquivo tempos_medios.csv
tamanhos = [100, 10000, 1000000]
tempos_python = [0.0003, 0.025, 2.3]
desvios_python = [0.00005, 0.002, 0.12]
tempos_java = [0.0001, 0.012, 1.2]
desvios_java = [0.00002, 0.001, 0.08]

# Curvas teóricas de melhor e pior caso
melhor_caso = [n * np.log2(n) for n in tamanhos]  # O(n log n)
pior_caso = [n**2 for n in tamanhos]  # O(n²)

# Normalizar curvas teóricas para escala comparável
melhor_caso_normalizado = [x / max(melhor_caso) * max(tempos_python) for x in melhor_caso]
pior_caso_normalizado = [x / max(pior_caso) * max(tempos_python) for x in pior_caso]

# Gráfico: Python vs Curvas Teóricas
plt.figure(figsize=(8, 5))
plt.plot(tamanhos, melhor_caso_normalizado, label='Melhor Caso (O(n log n))', linestyle='--')
plt.plot(tamanhos, pior_caso_normalizado, label='Pior Caso (O(n²))', linestyle='--')
plt.errorbar(tamanhos, tempos_python, yerr=desvios_python, label='Python', marker='o', capsize=5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho da entrada (n)')
plt.ylabel('Tempo médio de execução (s)')
plt.title('Python: Comparação com Curvas Teóricas')
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig('python_vs_teorico.png')

# Normalizar curvas teóricas para escala comparável (Java)
melhor_caso_normalizado_java = [x / max(melhor_caso) * max(tempos_java) for x in melhor_caso]
pior_caso_normalizado_java = [x / max(pior_caso) * max(tempos_java) for x in pior_caso]

# Gráfico: Java vs Curvas Teóricas
plt.figure(figsize=(8, 5))
plt.plot(tamanhos, melhor_caso_normalizado_java, label='Melhor Caso (O(n log n))', linestyle='--')
plt.plot(tamanhos, pior_caso_normalizado_java, label='Pior Caso (O(n²))', linestyle='--')
plt.errorbar(tamanhos, tempos_java, yerr=desvios_java, label='Java', marker='s', capsize=5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho da entrada (n)')
plt.ylabel('Tempo médio de execução (s)')
plt.title('Java: Comparação com Curvas Teóricas')
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig('java_vs_teorico.png')

# Exibir ambos os gráficos
plt.show()
