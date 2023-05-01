#importar AVL
from AVL import AVLTree, Node
import random

# create an empty AVL tree
avl_tree = AVLTree()

#check the loop is inserting all the nodes given
arr = []

print('\n*** Inserting Nodes in Tree ***\n')

#insert known values to test code
#node_values = [9,12, 10, 4, 11, 16, 55, 5, 1, 2]
#node_values = [9,22, 10, 4, 11, 16, 2, 5, 56, 59]
#node_values = [77,12, 10, 4, 11, 16, 55, 5, 63, 2]

#insert values at random, you can n to make it the quantity of nodes you want
n = 200
node_values = [random.randint(1, 100) for _ in range(n)]
# insert some values using a loop
for value in node_values:
    print('Inserting node with value: {}'.format(value))
    arr.append(value)
    avl_tree.insert(value)


print(arr)
print('\n*** Searching Nodes in Tree ***\n')

# search for a value
print(avl_tree.search(63))
print(avl_tree.search(4))  
print(avl_tree.search(6))  
print(avl_tree.search(77))  
print(avl_tree.search(5))  
print(avl_tree.search(22))  
print(avl_tree.search(10))  

print('\n*** Checking Positions of Nodes in Tree ***\n')
#just to check if all the values are actually where they're supposed to pero si no existe da un traceback
print(avl_tree.root)
print(avl_tree.root.left_child)
print(avl_tree.root.right_child)



print('\n*** Traverse Nodes in Tree ***\n')

# call traverse_in_order to get the values in the AVL tree in order
values_in_order = avl_tree.traverse_in_order()

# print the values in order
print(values_in_order)

#para visualizar el AVL crea un .pdf
print('\n*** Graph Nodes in Tree ***\n')
dot = avl_tree.to_graphviz()
dot.render("AVL-TREE.gv", view=True)