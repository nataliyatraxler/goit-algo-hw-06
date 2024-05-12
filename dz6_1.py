import networkx as nx
import matplotlib.pyplot as plt
# Створимо порожній граф
G = nx.Graph()

# Додамо вершини (перехрестя)
intersections = [1, 2, 3, 4, 5, 6, 7]

# Додамо ребра (вулиці)
streets = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 6), (5, 7), (6, 7)]

# Додамо вершини та ребра до графа
G.add_nodes_from(intersections)
G.add_edges_from(streets)
nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', node_size=700)
plt.show()
# Виведемо основні характеристики графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вершин:", dict(G.degree()))