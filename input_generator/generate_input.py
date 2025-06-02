import random
import os

def gerar_lista(tamanho, limite=1000000):
    return [random.randint(0, limite) for _ in range(tamanho)]

if __name__ == "__main__":
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for tamanho in [100, 10000, 1000000]:
        lista = gerar_lista(tamanho)
        caminho_arquivo = os.path.join(raiz, f"entrada_{tamanho}.txt")
        with open(caminho_arquivo, "w") as f:
            f.write(" ".join(map(str, lista)))
        print(f"Arquivo {caminho_arquivo} gerado com sucesso.")