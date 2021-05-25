import networkx as nx
import matplotlib.pyplot as plt
import random, math


def make_graph(size: int, seed: int):
    N = size
    random.seed(seed)
    data = {i: [random.randrange(0, 100) for _ in range(2)] for i in range(N)}
    g = nx.Graph()
    for i, d in enumerate(data):
        g.add_node(i)
    return g, data


def dist_eu(x, y) -> int:
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

def solve(N, position):
    INF = 1001001001
    dp = [[INF] * (N - 1) for _ in range(2 ** (N - 1))]
    for i in range(N - 1):
        dp[1 << i][i] = dist_eu(position[0], position[i + 1])
    for s in range(1 << (N - 1)):
        for i in range(N - 1):
            if (s >> i) & 1:
                for j in range(N - 1):
                    if i == j or not (s & 1 << j):
                        continue
                    dp[s][i] = min(dp[s][i], dp[s - (1 << i)][j] + dist_eu(position[i+1], position[j+1]))
    res = INF
    end_v = None
    for i in range(N-1):
        if res > dp[2 ** (N - 1) - 1][i] + dist_eu(position[i + 1], position[0]):
            res = dp[2 ** (N - 1) - 1][i] + dist_eu(position[i + 1], position[0])
            end_v = i+1
    return dp, res, end_v


def restore(dp, v, N, position):
    edges = [(0, v)]
    s, v = 2 ** (N-1) - 1, v
    while v != 0 and s:
        next_s, next_v = None, None
        for i in range(N-1):
            if i != (v-1) and (1 << i) & s:
                if math.isclose(dp[s][v-1], dp[s - (1<<(v-1))][i] +dist_eu(position[i+1], position[v])):
                    next_s, next_v = s - (1<<(v-1)), i+1
                    break
        if next_v is None:
            edges.append((v, 0))
            return edges
        edges.append((v, next_v))
        s, v = next_s, next_v


def plot_before_after(g, node_color, position):
    # before
    nx.draw_networkx(g, edge_color='w', pos=position, node_color=node_color)
    plt.axis('off')
    plt.show()

    # after
    nx.draw_networkx(g, edge_color='red', pos=position, node_color=node_color)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    # N: 頂点数
    # g: 無向グラフ, position: 頂点座標の配列
    # dp: dp配列, min_value: 最短時長, end_v: 終点
    # edges: 最短サイクルの辺集合

    N = 15
    g, position = make_graph(size=N, seed=4)
    dp, min_value, end_v = solve(N, position)
    edges = restore(dp, end_v, N, position)
    g.add_edges_from(edges)
    node_color = ['coral' if node == 0 else 'lightblue' for node in g.nodes.keys()]
    plot_before_after(g, node_color=node_color, position=position)
