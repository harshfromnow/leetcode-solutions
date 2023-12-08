int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* result=(int*)malloc(2*sizeof(int));
    int beg=0;
    int end=numbersSize-1;
    while(beg<end){
        int sum=numbers[beg]+numbers[end];
        if (sum==target){
            result[0]=beg+1;
            result[1]=end+1;
            *returnSize=2;
            return result;
        }
        else if (sum<target) beg++;
        else if (sum>target) end--;
    }
    free(result);
    *returnSize=0;
    return NULL;
}
