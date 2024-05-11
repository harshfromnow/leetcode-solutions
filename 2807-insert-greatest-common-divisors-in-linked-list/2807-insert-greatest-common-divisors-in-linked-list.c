/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int gcd(int a, int b){
    if (b==0)
        return a;
    else
        return gcd(b,a%b);
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
    if (head == NULL)
        return NULL;
    struct ListNode* current = head;
    while (current->next != NULL){
        struct ListNode* num = malloc(sizeof(struct ListNode));
        num->val = gcd(current->val, current->next->val);
        num->next = current->next;
        current->next = num;
        current = current->next->next; // Skip the newly inserted node
    }
    return head;
}
