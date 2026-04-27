#ifdef T1
int height(BSTNode *root) {
    // TODO: Complete this function
    // TODO 1 BEGIN
    
    if (root == NULL) return 0;
    
    int l = 0;
    int r = 0;

    if (root->left == NULL && root->right == NULL) return 1;  
    
    if (root->left != NULL) l += height(root->left) + 1;    
    if (root->right != NULL) r += height(root->right) + 1;    

    return (l >= r) ? l : r;
    
    // TODO 1 END
}
#endif


#ifdef T2
int count_nodes_at_level(BSTNode *root, int k) {
    // TODO: Complete this function
    // TODO 2 BEGIN
    
    if (root == NULL) return 0;

    int amt = 0;
    
    if (k == 0) return 1;    

    if (root->left != NULL) amt += count_nodes_at_level(root->left, k-1);
    if (root->right != NULL) amt += count_nodes_at_level(root->right, k-1);
    
    return amt; 
    
    // TODO 2 END
}
#endif

