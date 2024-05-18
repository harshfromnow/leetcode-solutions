/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void flatten(struct TreeNode* root) {
    if (root==NULL){
        return;
    }
    while (root!=NULL){
        if (root->left!=NULL){
            struct TreeNode* l=root->left;
            while(l->right!=NULL){
                l=l->right;
            }
            l->right=root->right;
            root->right=root->left;
            root->left=NULL;
        }
        root=root->right;
    }
    return;
}