bool isValid(char* s) {

    int i,n=0;
    while (s[n]!='\0'){
        n++;
    }
    int top=0;
    char* stack = (char*)malloc(n * sizeof(char));
    for (int i=0;i<n;i++){
        if (s[i]=='(' || s[i]=='[' || s[i]=='{'){
            stack[top]=s[i];
            top++;
        }
        else if (top>0 && ((s[i] == ')' && stack[top - 1] == '(') ||
                    (s[i] == ']' && stack[top - 1] == '[') ||
                    (s[i] == '}' && stack[top - 1] == '{'))) 
            top--;
        else{
            free(stack);
            return false;
        }
    }
    free(stack);
    return top==0;
}
