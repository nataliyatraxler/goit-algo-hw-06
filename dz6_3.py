import networkx as nx

# Створення графа з вагами
G = nx.Graph()
edges = [
    (1, 2, 1.5), (1, 3, 2.0), (2, 4, 2.5), 
    (2, 5, 1.0), (3, 6, 1.2), (4, 6, 2.2), 
    (5, 7, 0.8), (6, 7, 1.6)
]
G.add_weighted_edges_from(edges)

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів
lengths = dict(nx.all_pairs_dijkstra_path_length(G))

# Вивід найкоротших шляхів від вершини 1 до усіх інших вершин
for target in lengths[1]:
    print(f"Найкоротший шлях від вершини 1 до {target} є {lengths[1][target]} одиниць довжини")

# Додатково можна вивести всі найкоротші шляхи
paths = dict(nx.all_pairs_dijkstra_path(G))
print("\nУсі найкоротші шляхи від вершини 1:")
for target, path in paths[1].items():
    print(f"Шлях до {target}: {path}")
