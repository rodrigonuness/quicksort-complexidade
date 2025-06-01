import time
import random
import statistics

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def medir_tempo(n, execucoes=30):
    tempos = []
    for _ in range(execucoes):
        arr = [random.randint(0, n) for _ in range(n)]
        inicio = time.time()
        quicksort(arr)
        fim = time.time()
        tempos.append(fim - inicio)
    return sum(tempos)/len(tempos), statistics.stdev(tempos)

if __name__ == "__main__":
    for tamanho in [100, 10000, 1000000]:
        media, desvio = medir_tempo(tamanho)
        print(f"Tamanho: {tamanho}, Tempo médio: {media:.5f}s, Desvio: {desvio:.5f}s")
