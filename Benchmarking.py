# Aqui vamos a hacer un apartado para el benchmarking

import time
import random
from AVL import AVLTree
from binary_search_tree import BinarySearchTree

# Cantidad de valores a insertar
N = 100000

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
    left_value = get_value_at_index(node.left_child, index, current_index)
    if left_value is not None:
        return left_value

    # Verificar si el valor actual es el buscado
    if current_index == index:
        return node.data

    current_index += 1

    # Recorrer subárbol derecho
    right_value = get_value_at_index(node.right_child, index, current_index)
    if right_value is not None:
        return right_value

    return None

# Se define una lista de tuplas que contiene información sobre las búsquedas que se realizarán
# Cada tupla tiene cuatro elementos:
# - El nombre de la búsqueda.
# - Una función que realiza la búsqueda en un árbol AVL.
# - Una función que realiza la búsqueda en un árbol BST.
# - Un valor de búsqueda (opcional).

search_values = [
    ("Valor máximo", lambda: avl_tree.find_max(avl_tree.root), lambda: bst.find_max(bst.root), None),
    ("Valor medio", lambda: get_value_at_index(avl_tree.root, (N - 1) // 2, 0), lambda: get_value_at_index(bst.root, (N - 1) // 2, 0), None),
    ("Valor inexistente", lambda: avl_tree.search(N * 100), lambda: bst.search(N * 100), None),
    ("Valor aleatorio", lambda: avl_tree.search(random.choice(values)), lambda: bst.search(random.choice(values)), None),
    ("Valor mínimo", lambda: avl_tree.find_min(avl_tree.root), lambda: bst.find_min(bst.root), None),
]

# Se recorre la lista de búsquedas definida anteriormente
for name, avl_fn, bst_fn, search_val in search_values:

    # Se mide el tiempo que toma realizar la búsqueda en el árbol AVL
    start_time = time.perf_counter()
    avl_result = avl_fn()
    avl_time = time.perf_counter() - start_time

    # Se mide el tiempo que toma realizar la búsqueda en el árbol BST
    start_time = time.perf_counter()
    bst_result = bst_fn()
    bst_time = time.perf_counter() - start_time

    # Se comparan los resultados de ambas búsquedas
    if avl_result == bst_result:
        print(f"Búsqueda '{name}': los resultados son iguales")
    else:
        print(f"Búsqueda '{name}': los resultados son distintos")
    # Se imprimen los resultados y los tiempos de ambas búsquedas
    print(f"\tAVL: valor={avl_result}, tiempo={avl_time:.6f}s")
    print(f"\tBST: valor={bst_result}, tiempo={bst_time:.6f}s")

    # Si hay un valor de búsqueda definido, se realiza la búsqueda en ambos árboles y se miden los tiempos
    if search_val is not None:

        # Se mide el tiempo que toma realizar la búsqueda en el árbol AVL
        start_time = time.perf_counter()
        avl_tree.search(search_val)
        avl_time = time.perf_counter() - start_time

        # Se mide el tiempo que toma realizar la búsqueda en el árbol BST
        start_time = time.perf_counter()
        bst.search(search_val)
        bst_time = time.perf_counter() - start_time

        # Se imprimen los resultados y los tiempos de ambas búsquedas
        print(f"\tAVL: búsqueda de {search_val}, tiempo={avl_time:.6f}s")
        print(f"\tBST: búsqueda de {search_val}, tiempo={bst_time:.6f}s")

    if search_val is not None:

        # Se mide el tiempo que toma realizar la búsqueda en el árbol AVL
        val = random.choice(values) if search_val else N * 100
        start_time = time.perf_counter()
        avl_tree.search(val)
        avl_time = time.perf_counter() - start_time

        # Se mide el tiempo que toma realizar la búsqueda en el árbol BST
        start_time = time.perf_counter()
        bst.search(val)
        bst_time = time.perf_counter() - start_time

        # Se imprimen los resultados y los tiempos de ambas búsquedas
        print(f"\tAVL: búsqueda de {val}, tiempo={avl_time:.6f}s")
        print(f"\tBST: búsqueda de {val}, tiempo={bst_time:.6f}s")

    #assert avl_result == bst_result, f"Los resultados de la búsqueda '{name}' no coinciden en ambos árboles."


