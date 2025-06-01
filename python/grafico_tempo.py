import matplotlib.pyplot as plt

# Dados de exemplo, substitua pelos seus resultados reais se quiser
tamanhos = [100, 10000, 1000000]
tempos_python = [0.0003, 0.025, 2.3]
desvios_python = [0.00005, 0.002, 0.12]
tempos_java = [0.0001, 0.012, 1.2]
desvios_java = [0.00002, 0.001, 0.08]

plt.figure(figsize=(8,5))
plt.errorbar(tamanhos, tempos_python, yerr=desvios_python, label='Python', marker='o', capsize=5)
plt.errorbar(tamanhos, tempos_java, yerr=desvios_java, label='Java', marker='s', capsize=5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho da entrada (n)')
plt.ylabel('Tempo médio de execução (s)')
plt.title('Tempo de execução do Quick Sort')
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig('tempo_execucao.png')
plt.show()
