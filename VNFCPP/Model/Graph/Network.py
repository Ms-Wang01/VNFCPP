from VNFCPP.Model.Graph.EnhancedGraph import EnhancedGraph


class Network(EnhancedGraph):
    _latest_net_id = 0

    def __init__(self, incoming_graph_data=None, **kwargs):
        super().__init__(incoming_graph_data, **kwargs)
        Network._latest_net_id += 1
        self.network_id = Network._latest_net_id

