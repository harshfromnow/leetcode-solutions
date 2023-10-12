#include <stdio.h>

void swap(int A[], int i, int j) {
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
    return;
}

int partition(int A[], int p, int r) {
    int pivot = A[r];
    int i = p;
    for (int j = p; j < r; j++) {
        if (A[j] < pivot) {
            swap(A, i, j);
            i = i + 1;
        }
    }
    swap(A, i, r);
    return i;
}

int quickselect(int A[], int beg, int end, int k) {
    if (beg <= end) {
        int pivotindex = partition(A, beg, end);
        if (k == pivotindex) {
            return A[pivotindex];
        } else if (k < pivotindex) {
            return quickselect(A, beg, pivotindex - 1, k);
        } else {
            return quickselect(A, pivotindex + 1, end, k);
        }
    }
    return -1;  // Add a return statement in case of an invalid k
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int A[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }
    int kthSmallest = quickselect(A, 0, n - 1, k-1);
    if (kthSmallest != -1) {
        printf("kth smallest element is %d", kthSmallest);
    } else {
        printf("Invalid value of k.\n");
    }
    return 0;
}
