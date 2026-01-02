'''
# Docstring for 17_Binary_trees
- Binary tree is a specific/specialized kind of generic tree which can have atmost two children. 
- 0, 1 or 2 children allowed. 
- Why only two children allowed at max ?
1. It makes the structure a lot simpler than generic tree. 
2. Extremely useful for various computational purposes. 

# Real-Life examples:
1. yes/no decision making. 
2. Tournament Bracket. 
3. Family tree with two parent. 

# Industry examples:
1. Binary Decision Trees in AI/ML. 
2. Database Searching. 
3. Binary Trees in Compiler. 
'''

# Binary Tree Node.
# Each of left and right node is going to be a Binary Tree.

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)

# Print Binary Trees.
def print_binary_tree(root):

    if(root == None): # Base case. 
        return
    
    # Format: Node : L -> LeftChild Data, R -> RightChild Data
    print(root.data, end=": ")
    # Recursion can be used as each node in a binary sub-tree. 

    if(root.left != None):
        print(f"L->{root.left.data}", end=", ")
    else:
        print("L->None", end=",")
    
    if(root.right != None):
        print(f" R-> {root.right.data}")
    else:
        print("R->None")

    # Recurring for the left and right children. 
    print_binary_tree(root.left)
    print_binary_tree(root.right)

print_binary_tree(root)




