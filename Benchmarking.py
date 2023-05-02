# Aqui vamos a hacer un apartado para el benchmarking

import time
import random
from AVL import AVLTree
from binary_search_tree import BinarySearchTree

# Cantidad de valores a insertar
N = 1000#00

# Crear listas de valores aleatorios para insertar en ambos árboles
values = random.sample(range(N * 10), N)

# Crear árboles vacíos
avl_tree = AVLTree()
bst = BinarySearchTree()

# Insertar valores en ambos árboles
for value in values:
    avl_tree.insert(value)
    bst.insert(value)

# Función para obtener el valor que se encuentra en la mitad del árbol
def get_value_at_index(node, index, current_index):
    """
    Recorre el árbol en orden y devuelve el valor correspondiente al índice dado.
    """
    if not node:
        return None

    # Recorrer subárbol izquierdo
    left_value = get_value_at_index(node.left, index, current_index)
    if left_value is not None:
        return left_value

    # Verificar si el valor actual es el buscado
    if current_index == index:
        return node.value

    current_index += 1

    # Recorrer subárbol derecho
    right_value = get_value_at_index(node.right, index, current_index)
    if right_value is not None:
        return right_value

    return None

# Buscar valores en ambos árboles y medir el tiempo de ejecución
search_values = [
    ("Valor máximo", lambda: avl_tree.find_max(avl_tree.root), lambda: bst.find_max(bst.root)),
    ("Valor medio", lambda: get_value_at_index(avl_tree.root, (N - 1) // 2, 0), lambda: get_value_at_index(bst.root, (N - 1) // 2, 0)),
        print(f"Valores AVL: {avl_tree.traverse_in_order()}"),
        print(f"Valores BST: {bst.traverse(subtree=bst.root)}"),
    ("Valor inexistente", lambda: avl_tree.find(N * 100), lambda: bst.find(N * 100)),
    ("Valor aleatorio", lambda: avl_tree.find(random.choice(values)), lambda: bst.find(random.choice(values))),
    ("Valor mínimo", lambda: avl_tree.find_min(avl_tree.root), lambda: bst.find_min(bst.root)),
]

for name, avl_fn, bst_fn in search_values:
    start_time = time.time()
    avl_result = avl_fn()
    print(f"Valores AVL: {avl_tree.traverse_in_order()}"),




    start_time = time.time()
    bst_result = bst_fn()
    bst_time = time.time() - start_time

    assert avl_result == bst_result, f"Los resultados de la búsqueda '{name}' no coinciden en ambos árboles."

    print(f"Búsqueda '{name}':")
    print(f"\tAVL: tiempo={avl_time:.6f}s")
    print(f"\tBST: tiempo={bst_time:.6f}s")
