//descending order heapsort on character array
#include <stdio.h>
#include <string.h>

void minheapify(char *arr[], int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && strcmp(arr[left], arr[smallest]) < 0) {
        smallest = left;
    }

    if (right < n && strcmp(arr[right], arr[smallest]) < 0) {
        smallest = right;
    }

    if (smallest != i) {
        // Swap arr[i] and arr[smallest]
        char *temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;
        minheapify(arr, n, smallest);
    }
}

void buildMinHeap(char *arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        minheapify(arr, n, i);
    }
}

void heapSort(char *arr[], int n) {
    buildMinHeap(arr, n);

    for (int i = n - 1; i > 0; i--) {
        // Swap arr[0] and arr[i]
        char *temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        minheapify(arr, i, 0);
    }
}

int main() {
    char *arr[] = {"banana", "orange", "apple", "pineapple", "berries", "litchi"};
    int n = sizeof(arr) / sizeof(arr[0]);
    heapSort(arr, n);
    for (int i = 0; i < n; i++) {
        printf("%s ", arr[i]);
    }
    return 0;
}