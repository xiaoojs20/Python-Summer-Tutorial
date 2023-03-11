import networkx as nx
import matplotlib.pyplot as plt


# rela = [('张国立', '王刚', 30), ('张国立', '张铁林', 5), ('张国立', '黄晓明', 2)]
def draw_graph(rela_list, num_dict, file_name, tp='spring', max_node = 50):
    """
    rela_dict: 节点关系列表，比如：[('张国立', '王刚', 30), ('张国立', '张铁林', 5), ('张国立', '黄晓明', 2)]
    num_dict: 每个演员参与合作的电影数量比如：{'张国立':33,'王刚':30,'张铁林':5,'黄晓明':2}
    file_name: 输入的文件名称
    tp: 图形分布类型（circular/spring/shell/spectral）
    max_node：待显示的节点数量，默认是50个
    """

    plt.figure(figsize=(50, 50))

    for node in rela_list:
        print(node)

    print(max_node)
    if len(rela_list) > max_node:
        rela_list = sorted(rela_list, key = lambda x: x[2], reverse= True)
        rela_list = rela_list[0:max_node]
    for node in rela_list:
        print(node)

    # num_dict = {'甲':10, '乙':10, '丙':8, '丁':20}
    # num_dict = {}
    G = nx.Graph()
    for u, v, w in rela_list:
        G.add_edge(u, v, weight=w)
        # num_dict[v] = w/2
        # if u not in num_dict:
        #     num_dict[u] = w/2
        # else:
        #     num_dict[u] += w/2


    layout = tp + "_layout"

    attr = getattr(nx, layout)
    if not attr:
        print("can not find layout", tp)
        attr = nx.circular_layout
    pos = attr(G)
    # if tp == 'circular':
    #     pos = nx.circular_layout(G)  # 节点圆环分布
    # elif tp == 'spring':
    #     pos = nx.spring_layout(G)    # 节点放射分布
    # elif tp == 'shell':
    #     pos = nx.shell_layout(G)     # 节点同心圆分布，当节点较少时等同于圆环分布
    # elif tp == 'spectral':
    #     pos = nx.spectral_layout(G)    # 拉普拉斯特征向量分布
    # else:
    #     pos = nx.circular_layout(G)  # 节点圆环分布

    # 画边
    nx.draw_networkx_edges(G, pos, width=[d['weight'] for (u, v, d) in G.edges(data=True)], edge_color='green')
    # 画点
    # if num_dict:
    nx.draw_networkx_nodes(G, pos,  node_size= [(num_dict[node]) * 800 for node in G.nodes()], node_color='red')
    # nx.draw_networkx_nodes(G, pos,  node_size= [(num_dict[node]) * 200 for node in G.nodes()], with_label=True, node_color='red')
    # 标记
    nx.draw_networkx_labels(G, pos, font_size=40, font_color='black', font_family='simhei')
    # 画图
    # plt.rcParams['figure.figsize'] = (80.0, 40.0)
    plt.savefig(file_name)

import json
if __name__ == '__main__':
    rela_list = [('张国立', '王刚', 30), ('张国立', '张铁林', 5), ['张国立', '黄晓明', 2]]
    num_dict = {'张国立':33,'王刚':30,'张铁林':5,'黄晓明':2}
    # with open("rela_list.json", "rb") as f:
    #     rela_list = json.load(f)
    # print(len(rela_list))

    # print('rela_list', rela_list)
    # for idx, rela in enumerate(rela_list):
    #     print(idx, rela)
    # with open("num_dict.json", "rb") as f:
    #     num_dict = json.load(f)
    # print('num_dict', num_dict)
    # for p in num_dict:
    #     print(p, num_dict[p])

    draw_graph(rela_list, num_dict, "张国立", 'spring')
