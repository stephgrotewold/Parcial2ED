#Aqui tenemos un BST pque utilizaremos para poder hacer la comparacion en el benchmarking con el AVL tree.

'''
Binary Search Tree
'''

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        return '({})'.format(self.data)
    

class BinarySearchTree:

    def __init__(self):
        self.root = None
        """
        Create a new BinarySearchTree object | constructor.
        """

    def insert(self, value: int):
        """
        Insert a new value into the Binary Search Tree.

        Args:
            value (int): The value to be inserted.
        """
        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):
        """
        Recursively it will insert a new value into the Binary Search Tree.

        Args:
            value (int): The value to be inserted.
            subtree (Node): The root node of the subtree to insert into.
        """
        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        """
        Traverse the Binary Search Tree and print every node value.

        Args:
            subtree (Node): The root node of the subtree to traverse.
        """
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)


    def search(self, key: int) -> bool:
        """
        Search the Binary Search Tree for a specific "key".

        Args:
            key (int): The key to search for.

        Returns:
            bool: True if the key is found, if not... then is False.
        """
        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:
        """
        Recursively search a subtree for a specific "key".

        Args:
            key (int): The key to search for.
            subtree (Node): The root node of the subtree to search.

        Returns:
            bool: True if the key is found, if not... then is False.
        """
        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        

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


#-----------------------Delete Implementation--------------------------|        

    def delete(self, key: int) -> None:
            """
            Delete a node from the tree defined by the key.
            Args:
                key: The key of the node to delete.
            """

            if self.root is None:
                print('Tree is empty...')

            else:
                self._delete(key, self.root)


    def _delete(self, key: int, subtree: Node) -> None:
        """
        Delete a node from the tree defined by the key.
        Args:
            key: The key of the node to delete.
            subtree: The root of the subtree to delete from.
        """

        if key < subtree.data:
            if subtree.left_child is not None:
                self._delete(key, subtree.left_child)

            else:
                print('Key not found...')

        elif key > subtree.data:
            if subtree.right_child is not None:
                self._delete(key, subtree.right_child)

            else:
                print('Key not found...')

        else:
            if (subtree.left_child is None) and (subtree.right_child is None):
                subtree = None

            elif (subtree.left_child is None) and (subtree.right_child is not None):
                subtree = subtree.right_child

            elif (subtree.left_child is not None) and (subtree.right_child is None):
                subtree = subtree.left_child

            else:
                min_node = self.find_min(subtree.right_child)
                subtree.data = min_node.data
                self._delete(min_node.data, subtree.right_child)