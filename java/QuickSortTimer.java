import java.util.Random;

public class QuickSortTimer {

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    public static double medirTempo(int tamanho, int execucoes) {
        Random rand = new Random();
        double somaTempos = 0;

        for (int i = 0; i < execucoes; i++) {
            int[] arr = new int[tamanho];
            for (int j = 0; j < tamanho; j++) {
                arr[j] = rand.nextInt(tamanho);
            }
            long inicio = System.nanoTime();
            quickSort(arr, 0, tamanho - 1);
            long fim = System.nanoTime();
            somaTempos += (fim - inicio) / 1e9;
        }

        return somaTempos / execucoes;
    }

    public static void main(String[] args) {
        int[] tamanhos = {100, 10000, 1000000};
        int execucoes = 30;

        for (int tamanho : tamanhos) {
            double media = medirTempo(tamanho, execucoes);
            System.out.printf("Tamanho: %d, Tempo médio: %.5fs%n", tamanho, media);
        }
    }
}
