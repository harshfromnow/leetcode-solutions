//quicksort

#include <stdio.h>
void swap(int A[],int i, int j){
    int temp=A[i];
    A[i]=A[j];
    A[j]=temp;
    return;
}

int partition(int A[],int p,int r){
    int pivot=A[r];
    int i=p-1;
    for (int j=p;j<r;j++){
        if (A[j]<pivot){
            i=i+1;
            swap(A,i,j);
        }
    }
    swap(A,i+1,r);
    return i+1;
}

void quicksort(int A[],int p, int r){
    if (p<r){
        int q =partition(A,p,r);
        quicksort(A,p,q-1);
        quicksort(A,q+1,r);
    }
}

int main(){
    int n;
    printf("Enter number of elements: ");
    scanf("%d",&n);
    int A[n];
    printf("Enter %d integers:\n",n);
    for (int i=0 ; i<n ; ++i){
        scanf("%d", &A[i]);
    }
    quicksort(A,0,n-1);
    for (int i=0 ; i<n ; ++i){
        printf("%d ", A[i]);
    }
    return 1;
}