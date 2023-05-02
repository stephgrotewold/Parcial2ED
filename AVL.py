#aqui pongamos los metodos de insert,search, delete,min,max y traverse.

'''
Se requiere hacer los siguientes cambios del codigo del BSL para que sea un AVL

1) Cambiar la estructura de nodo a una estructura que contenga la altura del nodo y el factor de equilibrio.

2) Añadir una función para calcular la altura de un nodo, que tomará en cuenta la altura de sus subárboles.

3) Añadir una función para calcular el factor de equilibrio de un nodo, que se define como la diferencia de altura entre el subárbol derecho y el subárbol izquierdo.

4) Añadir las rotaciones necesarias (rotación simple y doble a la derecha y a la izquierda) para mantener el árbol equilibrado después de la inserción y eliminación de nodos.

5) Actualizar la altura y el factor de equilibrio de los nodos después de cada operación.
'''

from graphviz import Digraph
from typing import List
class Node:
    """
    A class representing a node in an AVL tree.
    
    Attributes
    ----------
    data : int
        The value stored in the node.
    left_child : Node
        The left child of the node.
    right_child : Node
        The right child of the node.
    height : int
        The height of the node.
    balance_factor : int
        The balance factor of the node.
    """

    def __init__(self, data: int) -> None:
        """
        Initializes a new Node object.

        Args:
            data (int): The value to be stored in the node.

        Attributes:
            data (int): The value stored in the node.
            left_child (Node): The left child of the node, initially set to None.
            right_child (Node): The right child of the node, initially set to None.
            height (int): The height of the node, initially set to 0.
            balance_factor (int): The balance factor of the node, initially set to 0.
        """
       
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0
        self.balance_factor = 0
    
    def __str__(self):
        """
        Return a string representation of the node's data value.

        Returns
        -------
        str
            A string representation of the node's data value.
        """
        return str(self.data)


class AVLTree:
    """
    A class that represents an AVL Tree.

    Attributes:
    - root (Node): The root node of the AVL Tree.

    Methods:
    - __init__(self)
        Constructs a new AVLTree instance.
        
    - get_height(self, node: Node) -> int:
        Returns the height of the given node. If the node is None, returns -1.

    - get_balance_factor(self, node: Node) -> int:
        Returns the balance factor of the given node.

    - update_height_and_balance_factor(self, node: Node) -> None:
        Updates the height and balance factor of the given Node.

    - rotate_left(self, node: Node) -> Node:
        Rotates the given node to the left and returns the new parent node.

    - rotate_right(self, node: Node) -> Node:
        Performs a right rotation on the given node and returns the new parent node.

    - rotate_left_right(self, node: Node) -> Node:
        Performs a left-right rotation on the given node.

    - rotate_right_left(self, node: Node) -> Node:
        Performs a right-left rotation on the subtree rooted at the given node.

    - insert(self, value: int) -> None:
        Inserts a new node with the given value into the AVL tree.

    - _insert(self, value: int, node: Node) -> Node:
        Recursively inserts a new node with the given value into the subtree rooted at the given node,
        and balances the tree if necessary. Returns the updated subtree after insertion and balancing.
    
    - to_graphviz(self):
        Generates a Graphviz representation of the AVL tree. Returns a Digraph object representing the AVL tree.

    - _to_graphviz(self, dot, node):
        Generates a Graphviz representation of the given node in the AVL tree
        and its children nodes.
    
    - search(self, value: int) -> bool:
        Searches for a node with the given value in the AVL tree. Returns a bool: True if a node with the given value exists, False otherwise.
    
    - _search(self, value: int, node: Node) -> bool:
        Recursively searches for a value in the AVL tree starting from the given node. Returns a bool, True if the value is found in the tree, False otherwise.
    
    - traverse_in_order(self) -> List[int]:
        Traverse the AVL tree in-order and return a list of all values in sorted order. Returns a list of all the values in the AVL tree in sorted order.
    
    - _traverse_in_order(self, node: Node, result: List[int]) -> None:
        Helper method to traverse the AVL tree in-order and append the values to a list.

    - delete(self, value: int) -> None:
        Deletes the node with the given value from the AVL tree.
    
    - _delete(self, value: int, node: Node) -> Node:
        Recursively deletes the node with the given value from the subtree rooted at the given node,
        and balances the tree if necessary. Returns the updated subtree after deletion and balancing.
    
    - find_min(self, node=None) -> int:
        Recursively finds and returns the minimum value in the subtree rooted at the given node.
    
    - find_max(self, node=None) -> int:
        Recursively finds and returns the maximum value in the subtree rooted at the given node.
    """   

    def to_graphviz(self):
        """
        Generates a Graphviz representation of the AVL tree.

        Returns:
            A Digraph object representing the AVL tree.
        """
        dot = Digraph(comment='AVL Tree')
        self._to_graphviz(dot, self.root)
        return dot

    def _to_graphviz(self, dot, node):
        """
        Generates a Graphviz representation of the given node in the AVL tree
        and its children nodes.

        Args:
            dot (Digraph): A Digraph object representing the AVL tree.
            node (AVLNode): The root node of the subtree to generate the
                Graphviz representation for.

        Returns:
            None
        """
        if node is None:
            return

        dot.node(str(node.data), str(node.data))
        if node.left_child is not None:
            dot.edge(str(node.data), str(node.left_child.data), label="Left")
            self._to_graphviz(dot, node.left_child)

        if node.right_child is not None:
            dot.edge(str(node.data), str(node.right_child.data), label="Right")
            self._to_graphviz(dot, node.right_child)

    def __init__(self):
        """
        Constructs a new AVLTree instance.

        Parameters:
            None

        Returns:
            None
        """
        self.root = None

    def get_height(self, node: Node) -> int:
        """
        Returns the height of the given node. If the node is None, returns -1.
        
        Args:
            node (Node): The node whose height needs to be returned.
        
        Returns:
            int: The height of the given node. If the node is None, returns -1.
        """
        if node is None:
            return -1
        else:
            return node.height

    def get_balance_factor(self, node: Node) -> int:
        """
        Returns the balance factor of the given node.
        
        Args:
        - node (Node): The node to calculate the balance factor of
        
        Returns:
        - int: The balance factor of the node
        """
        if node is None:
            return 0
        else:
            return self.get_height(node.left_child) - self.get_height(node.right_child)

    def update_height_and_balance_factor(self, node: Node) -> None:
        """
        Updates the height and balance factor of the given Node.

        Args:
            node (Node): The Node whose height and balance factor are to be updated.

        Returns:
            None.
        """
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        node.balance_factor = self.get_balance_factor(node)

    def rotate_left(self, node: Node) -> Node:
        """
        Rotates the given node to the left and returns the new parent node.
            
        Args:
            node (Node): The node to rotate.
            
        Returns:
            Node: The new parent node.
        """
        new_parent = node.right_child
        node.right_child = new_parent.left_child
        new_parent.left_child = node

        self.update_height_and_balance_factor(node)
        self.update_height_and_balance_factor(new_parent)

        return new_parent

    def rotate_right(self, node: Node) -> Node:
        """
        Performs a right rotation on the given node and returns the new parent node.

        Args:
            node (Node): The node to perform the right rotation on.

        Returns:
            Node: The new parent node after the right rotation.
        """
        new_parent = node.left_child
        node.left_child = new_parent.right_child
        new_parent.right_child = node

        self.update_height_and_balance_factor(node)
        self.update_height_and_balance_factor(new_parent)

        return new_parent

    def rotate_left_right(self, node: Node) -> Node:
        """
        Performs a left-right rotation on the given node.

        Args:
            node (Node): The node to be rotated.

        Returns:
            Node: The new parent node resulting from the rotation.
        """
        node.left_child = self.rotate_left(node.left_child)
        return self.rotate_right(node)

    def rotate_right_left(self, node: Node) -> Node:
        """
        Performs a right-left rotation on the subtree rooted at the given node.

        Args:
            node (Node): The root node of the subtree to rotate.

        Returns:
            Node: The new root node of the rotated subtree.
        """
        node.right_child = self.rotate_right(node.right_child)
        return self.rotate_left(node)

    def insert(self, value: int) -> None:
        """
        Inserts a new node with the given value into the AVL tree.

        Args:
        - value (int): The value to be inserted.

        Returns:
        - None
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(value, self.root)

    def _insert(self, value: int, node: Node) -> Node:
        """
        Recursively inserts a new node with the given value into the subtree rooted at the given node,
        and balances the tree if necessary. Returns the updated subtree after insertion and balancing.
        
        Args:
        - value (int): The value to be inserted into the tree.
        - node (Node): The root of the subtree where the new node is to be inserted.
        
        Returns:
        - Node: The root of the updated subtree after insertion and balancing.
        """
        if value < node.data:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                node.left_child = self._insert(value, node.left_child)

            # Check if the balance factor of the node is greater than 1
            if self.get_balance_factor(node) > 1:
                # Check if the balance factor of the left child is less than 0
                if self.get_balance_factor(node.left_child) < 0:
                    node = self.rotate_left_right(node)
                else:
                    node = self.rotate_right(node)

        elif value > node.data:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                node.right_child = self._insert(value, node.right_child)

            # Check if the balance factor of the node is less than -1
            if self.get_balance_factor(node) < -1:
                # Check if the balance factor of the right child is greater than 0
                if self.get_balance_factor(node.right_child) > 0:
                    node = self.rotate_right_left(node)
                else:
                    node = self.rotate_left(node)

        # Update the height and balance factor of the node
        self.update_height_and_balance_factor(node)

        return node

    def search(self, value: int) -> bool:
        """
        Searches for a node with the given value in the AVL tree.
        
        Args:
        - value (int): The value to search for in the tree.
        
        Returns:
        - bool: True if a node with the given value exists in the tree, False otherwise.
        """
        return self._search(value, self.root)

    def _search(self, value: int, node: Node) -> bool:
        """
        Recursively searches for a value in the AVL tree starting from the given node.

        Args:
            value (int): The value to search for.
            node (Node): The root node to start the search from.

        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        if node is None:
            return False
        elif value == node.data:
            return True
        elif value < node.data:
            return self._search(value, node.left_child)
        else:
            return self._search(value, node.right_child)


    def traverse_in_order(self) -> List[int]:
        """
        Traverse the AVL tree in-order and return a list of all values in sorted order.
        
        Returns:
            List[int]: A list of all values in the AVL tree in sorted order.
        """
        result = []
        self._traverse_in_order(self.root, result)
        return result

    def _traverse_in_order(self, node: Node, result: List[int]) -> None:
        """
        Helper method to traverse the AVL tree in-order and append the values to a list.
        
        Args:
            node (Node): The root node of the subtree to traverse.
            result (List[int]): The list to append the values to.
        """
        if node is not None:
            self._traverse_in_order(node.left_child, result)
            result.append(node.data)
            self._traverse_in_order(node.right_child, result)


#-----------------------------------------------------------------------------------------------------------------
    def delete(self, value: int) -> None:
        """
        Deletes the node with the given value from the AVL tree.

        Args:
            value (int): The value of the node to be deleted.

        Returns:
            None
        """
        self.root = self._delete(value, self.root)

    def _delete(self, value: int, node: Node) -> Node:
        """
        Recursively deletes the node with the given value from the subtree rooted at the given node,
        and balances the tree if necessary. Returns the updated subtree after deletion and balancing.

        Args:
            value (int): The value of the node to be deleted.
            node (Node): The root of the subtree where the node is to be deleted.

        Returns:
            Node: The root of the updated subtree after deletion and balancing.
        """
        if node is None:
            return node

        if value < node.data:
            node.left_child = self._delete(value, node.left_child)
        elif value > node.data:
            node.right_child = self._delete(value, node.right_child)
        else:
            # Case 1: Node has no child or only one child
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            # Case 2: Node has two children
            else:
                # Get the node with the next smallest value (in-order successor)
                successor_node = node.right_child
                while successor_node.left_child is not None:
                    successor_node = successor_node.left_child

                # Replace the node's data with the successor node's data
                node.data = successor_node.data

                # Delete the successor node from the right subtree
                node.right_child = self._delete(successor_node.data, node.right_child)

        # Update the height and balance factor of the node
        self.update_height_and_balance_factor(node)

        # Balance the node if necessary
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1:
            if self.get_balance_factor(node.left_child) < 0:
                node = self.rotate_left_right(node)
            else:
                node = self.rotate_right(node)
        elif balance_factor < -1:
            if self.get_balance_factor(node.right_child) > 0:
                node = self.rotate_right_left(node)
            else:
                node = self.rotate_left(node)

        return node


    
    def find_min(self, subtree: Node) -> int:
        """
        Find the "min" value in a subtree.

        Args:
            subtree (Node): The root node of the subtree to search.

        Returns:
            int: The minimum value in the subtree.
        """
        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree.data



        

    def find_max(self, subtree: Node) -> int:
        """
        Find the "max" value in a subtree.

        Args:
            subtree (Node): The root node of the subtree to search.

        Returns:
            int: The maximum value in the subtree.
        """
        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree.data

