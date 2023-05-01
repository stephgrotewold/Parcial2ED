
from typing import List
#aqui pongamos los metodos de insert,search, delete,min,max y traverse.


'''
Se requiere hacer los siguientes cambios del codigo del BSL para que sea un AVL

1) Cambiar la estructura de nodo a una estructura que contenga la altura del nodo y el factor de equilibrio.

2) Añadir una función para calcular la altura de un nodo, que tomará en cuenta la altura de sus subárboles.

3) Añadir una función para calcular el factor de equilibrio de un nodo, que se define como la diferencia de altura entre el subárbol derecho y el subárbol izquierdo.

4) Añadir las rotaciones necesarias (rotación simple y doble a la derecha y a la izquierda) para mantener el árbol equilibrado después de la inserción y eliminación de nodos.

5) Actualizar la altura y el factor de equilibrio de los nodos después de cada operación.
'''
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
    """   

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
            return "No ta' el {} en nuestro arbolito".format(value)
        elif value == node.data:
            return "Si existe el {} en el arbolito".format(value)
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