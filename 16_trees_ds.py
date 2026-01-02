'''
# Docstring for 16_trees_ds
- Non-Linear Data Structure.
- Tree is a Heirarchial data structure consisting of nodes which are connected by edges.

1. Node - Each item of my tree. 
2. Edges - Connnection between 2 nodes. 
3. Root - Topmost node. 
4. Leaf - Node with no-childrens. 
5. Parent - 
6. Child - 
7. Ancestors - 
8. Descendants - 
9. Subtree - 
10. Level/Depth - 
11. Path - Sequence of nodes and edges connecting one node to another. 
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode(1)

child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

print(root.children[0].data)

# Print tree using Recursion. 
def print_tree(root):
    
    print(root.data)

    for eachChild in root.children:
        print_tree(eachChild)

print_tree(root)


