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

# Take Input of a Binary Trees. 
def take_input_binary_tree():
    data = int(input("Enter the data for the node: "))

    if(data == -1):
        return None

    node = BinaryTreeNode(data)

    print(f"Enter the left child of {data}: ")
    node.left = take_input_binary_tree()

    print(f"Enter the right child of {data}: ")
    node.right = take_input_binary_tree()

    return node

print("Enter the Binary Tree Data (-1 for No Node): ")
root = take_input_binary_tree()
print_binary_tree(root)

# Take input level-wise. 
from collections import deque

def take_input_level_wise():
    data = int(input("Enter the data for the Root: "))
    if(data == -1):
        return None
    
    root = BinaryTreeNode(data)
    queue = deque([root])

    while len(queue) != 0:
        current_node = queue.popleft()

        left_child_data = int(input(f"Enter left child for {current_node.data} : "))
        if(left_child_data != -1):
            left_node = BinaryTreeNode(left_child_data)
            current_node.left = left_node
            queue.append(left_node)

        right_child_data = int(input(f"Enter right child for {current_node.data} : "))
        if(right_child_data != -1):
            right_node = BinaryTreeNode(right_child_data)
            current_node.right = right_node
            queue.append(right_node)

    return root

print("Enter the Binary Tree Data (-1 for No Node): ")
root = take_input_level_wise()
print_binary_tree(root)

def print_BinaryTree_Levelwise(root):
    pass


# Diameter of a tree: Maximum distance between points.
'''
# 3 Scenarios. 
1. Diameter through root. 
    leftheight + rightHeight = diameter
2. left diameter
3. right diameter

Note: Diameter can consist of nodes not passing through root.
'''
# Complexity of Height function is O(n).
def height(root):
    if(root != None):
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    heightOfTree = 1 + max(left_height, right_height)

    return heightOfTree

def diameter_of_a_tree(root):
    if(root == None):
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    left_diameter = diameter_of_a_tree(root.left)
    right_diameter = diameter_of_a_tree(root.right)

    maxDiameter = max(left_diameter, right_diameter, leftHeight+rightHeight)

    return maxDiameter

diameter_of_a_tree(root)

# Diameter of Tree - Optimized Manner.
# 2 calls for some information. 
# 1. Height
# 2. diameter
# Instead of just asking height, We will ask children to get both height and diameter. 

def diameter_of_tree_optimized(root):
    if(root == None):
        return 0, 0 # height, diameter
    
    left_height, left_diameter = diameter_of_tree_optimized(root.left)
    right_height, right_diameter = diameter_of_tree_optimized(root.right)
    
    # Option: 1
    diameter_through_root = left_height + right_height

    # Option: 2 left diameter

    # Option: 3 right diameter

    ans_diameter = max(diameter_through_root, left_diameter, right_diameter)

    current_tree_height = 1 + max(left_height, right_height)

    return current_tree_height, ans_diameter

treeHeight, treeDiameter = diameter_of_tree_optimized(root)
print(treeHeight, treeDiameter)

# Balance Binary Trees. 
def is_binary_tree_balanced(root):
    if(root == None):
        return


# Traversal in Binary Trees.
# 1. Preorder: first parent and then child. 
# Always, we call left first and then right because order matters in binary trees. 

def preorder_traversal(root):
    if(root == None):
        return
    
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

preorder_traversal(root)

def postorder_traversal(root):
    if(root == None):
        return
    # first my children and then me. 
    postorder_traversal(root.left)
    postorder_traversal(root.right)

    print(root.data, end=" ")

postorder_traversal(root)

def inorder_traversal(root):
    if(root == None):
        return
    # first the left, then me, then right, left child -> parent -> rightChild.
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

inorder_traversal(root)




