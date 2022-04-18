#!/usr/bin/python3
# The main code of the Simulator
from VNFCPP.Model.Graph.EnhancedGraph import EnhancedGraph
import networkx as nx
from VNFCPP.Model.Graph.Link import VirtualLink
from VNFCPP.Model.Graph.Network import Network
from VNFCPP.Model.Graph.Requirement import Specs, VNFRequirement
from VNFCPP.Model.Graph.ServiceChain import ServiceChain
from VNFCPP.Model.Graph.VNF import VNF
import matplotlib.pyplot as plt


def test1():
    # Create a service chain named sc1 and plot its topology
    spec1 = Specs(cpu=2, memory=2000, storage=200)
    spec2 = Specs(cpu=1, memory=1000, storage=100)
    vnf_req1 = VNFRequirement(specs=spec1, processing_delay=1e-6)
    vnf_req2 = VNFRequirement(specs=spec2, processing_delay=2e-6)
    vnf1 = VNF(vnf_name="VNF1", vnf_requirement=vnf_req1)
    vnf2 = VNF(vnf_name="VNF2", vnf_requirement=vnf_req2)
    vnf3 = VNF(vnf_name="VNF3", vnf_requirement=vnf_req1)

    sc1 = ServiceChain(name="sc1")
    sc1.add_vnf(vnf1, name=vnf1.vnf_name, label=vnf1.vnf_name)
    sc1.add_vnf(vnf2, name=vnf2.vnf_name, label=vnf2.vnf_name)
    sc1.add_vnf(vnf3, name=vnf3.vnf_name, label=vnf3.vnf_name)

    v_link1 = VirtualLink(source=vnf1, target=vnf2)
    print(v_link1)
    v_link2 = VirtualLink(source=vnf2, target=vnf3)

    sc1.add_edge(vnf1, vnf2, object=v_link1, weight=1)
    sc1.add_edge(vnf2, vnf3, object=v_link2, weight=2)

    for vnf in sc1.nodes:
        print(vnf)

    for vlink in sc1.edges:
        print(vlink)

    print(nx.dijkstra_path(sc1, vnf1, vnf3))
    for vnf in nx.dijkstra_path(sc1, vnf1, vnf3):
        print(vnf.vnf_name)

    options = {
        'node_color': 'orange',
        'node_size': 2000,
        'width': 5,
    }

    nx.draw(sc1, with_labels=True, **options)
    plt.savefig("output/sc1.png")


def main():
    test1()


if __name__ == '__main__':
    main()
