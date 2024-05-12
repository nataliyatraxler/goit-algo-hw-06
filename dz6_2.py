import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
intersections = [1, 2, 3, 4, 5, 6, 7]
streets = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 6), (5, 7), (6, 7)]
G.add_nodes_from(intersections)
G.add_edges_from(streets)

# Візуалізація графа
nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', node_size=700)
plt.show()

# Виконання DFS
dfs_path = list(nx.dfs_edges(G, source=1))
print("DFS від вершини 1:", dfs_path)

# Виконання BFS
bfs_path = list(nx.bfs_edges(G, source=1))
print("BFS від вершини 1:", bfs_path)

# Порівняння результатів DFS та BFS
print("\nПорівняння DFS та BFS:")
print("DFS дає наступний порядок обходу ребер:", dfs_path)
print("BFS дає наступний порядок обходу ребер:", bfs_path)

# Обговорення результатів
print("\nОбговорення результатів:")
print("DFS занурюється глибоко до одного вузла, перш ніж рухатися до наступного, що може призвести до більш розгалуженого шляху.")
print("BFS рівномірно відвідує всі сусідні вузли, перш ніж перейти на наступний рівень, забезпечуючи більш збалансований обхід.")
