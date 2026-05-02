# Phase 1 Extraction: Trees (BST & AVL)

## 1. Theoretical Core: Core Concepts

### Binary Search Trees (BST)
- **Properties**: A hierarchical, node-based structure where for any given node `y`:
  - All nodes in its left subtree have values less than or equal to `y.data` (`x.data <= y.data`).
  - All nodes in its right subtree have values strictly greater than `y.data` (`z.data > y.data`).
- **Insertion**: Takes advantage of the BST property to find an empty leaf position. The process involves traversing down the tree (left if smaller, right if larger) until a `NULL` child pointer is reached, where the new node is attached.
- **Deletion**: Requires careful pointer manipulation to maintain the BST property. It handles three scenarios based on the target node's children:
  - **No Children (Leaf)**: The simplest case; remove the node and set the parent's pointer to `NULL`.
  - **One Child**: "Promote" the target's single child to take its place by updating the grandparent's pointer.
  - **Two Children**: Find the **successor** (minimum value in the right subtree) or **predecessor** (maximum value in the left subtree). Overwrite the target node's data with the successor/predecessor's data, then recursively delete that successor/predecessor node (which will fall into the 0 or 1 child scenario).

### AVL Trees
- **Properties**: A self-balancing BST that ensures the tree's height remains $O(\log n)$, preventing the catastrophic $O(n)$ linear degeneration that can occur in standard BSTs when data is inserted in sorted order.
- **Balance Factor (BF)**: The metric used to trigger rebalancing, calculated for each node as $Height_{Left} - Height_{Right}$. Valid BFs are -1, 0, and +1. If a node's BF reaches -2 or +2 after a modification, rotations are necessary. (Note: The height of an empty tree/subtree is mathematically defined as -1).
- **Rotations**: Corrective structural changes applied locally when an imbalance is detected.
  - **LL Configuration** (Left-Left): Pivot BF is +2, Left Child BF is +1 (or 0). Fixed with a **Single Right Rotation** at the pivot.
  - **RR Configuration** (Right-Right): Pivot BF is -2, Right Child BF is -1 (or 0). Fixed with a **Single Left Rotation** at the pivot.
  - **LR Configuration** (Left-Right): Pivot BF is +2, Left Child BF is -1. Fixed with a **Left Rotation at the left child**, followed by a **Right Rotation at the pivot**.
  - **RL Configuration** (Right-Left): Pivot BF is -2, Right Child BF is +1. Fixed with a **Right Rotation at the right child**, followed by a **Left Rotation at the pivot**.

## 2. Algorithmic Tracing: AVL RL Double Rotation
**Scenario**: Inserting values **10, 30, 20** into an initially empty AVL tree.
1. **Insert 10**: Becomes the root. Tree is balanced (BF = 0).
2. **Insert 30**: Added as the right child of 10. Node 10's BF becomes -1. Tree is balanced.
3. **Insert 20**: Added as the left child of 30.
   - Node 20: Height = 0, BF = 0.
   - Node 30: Height = 1, $H_L(0) - H_R(-1) = +1$. BF = +1 (Left-heavy).
   - Node 10 (Root): Height = 2, $H_L(-1) - H_R(1) = -2$. BF = -2 (Right-heavy).
   - **Imbalance detected at Pivot 10.** The configuration is Right-Left (RL) because the pivot is right-heavy (-2) but its right child (30) is left-heavy (+1).
4. **Rebalancing (RL Double Rotation)**:
   - **Step 1: Right Rotation at child (30)**. Node 20 moves up, 30 becomes its right child. Node 10's right child is now 20.
   - **Step 2: Left Rotation at pivot (10)**. Node 20 becomes the new root. 10 becomes the left child of 20, and 30 remains the right child of 20.
5. **Final State**: Root is 20 (BF=0). Left child 10 (BF=0). Right child 30 (BF=0). The tree is perfectly balanced.

## 3. Code Implementation: C Snippets

### BST Insertion (Recursive)
```c
BSTNode* insertRec(BSTNode* root, int value) {
    if (root == NULL) {
        BSTNode* newNode = (BSTNode*)malloc(sizeof(BSTNode));
        newNode->data = value;
        newNode->left = NULL;
        newNode->right = NULL;
        return newNode;
    }
    
    // Traverse to find the empty slot
    if (value < root->data) {
        root->left = insertRec(root->left, value);
    } else if (value > root->data) {
        root->right = insertRec(root->right, value);
    }
    
    return root;
}
```

### AVL Rotations (LL and RR)
```c
// Helper function to safely get the height of a node
int getHeight(AVLNode *n) {
    if (n == NULL) return -1;
    return n->height;
}

// Single Right Rotation (Fixes LL Configuration)
AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;

    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights (must update child 'y' before parent 'x')
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;

    return x; // Return the new root of this subtree
}

// Single Left Rotation (Fixes RR Configuration)
AVLNode* leftRotate(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;

    // Perform rotation
    y->left = x;
    x->right = T2;

    // Update heights (must update child 'x' before parent 'y')
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;

    return y; // Return the new root of this subtree
}
```

## 4. Skills & Pitfalls
- **Forgetting to update height**: During any modification (insertion, deletion) and strictly after every rotation, heights must be updated bottom-up. Failing to update heights leads to incorrect balance factor calculations, entirely breaking the AVL tree's self-balancing mechanism.
- **Incorrect parent pointer updates**: If your structure includes explicit `parent` pointers, rotations become significantly more complex. A common pitfall is forgetting to properly reassign the parent pointers of the nodes being rotated and the subtrees being transferred (e.g., `T2` in the rotation snippets).
- **Failing to check all ancestors**: After an insertion or deletion, you must trace the path back up to the root, updating heights and calculating balance factors. While an insertion causes at most one imbalance that needs fixing, a **deletion can cause cascading imbalances** all the way up the tree. Stopping the check after the first rotation during a deletion is a critical flaw.