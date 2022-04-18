import networkx as nx
from abc import ABC, abstractmethod


class EnhancedGraph(nx.Graph, ABC):

    def __init__(self, incoming_graph_data=None, **kwargs):
        super().__init__(incoming_graph_data, **kwargs)


shortest_path = nx.shortest_path
