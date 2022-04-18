from abc import ABC, abstractmethod


class Node(ABC):
    _latest_node_id = 0

    def __init__(self):
        Node._latest_node_id += 1
        self.node_id = Node._latest_node_id


class PhysicalNode(Node, ABC):
    _latest_physical_node_id = 0

    def __init__(self):
        super().__init__()
        PhysicalNode._latest_physical_node_id += 1
        self.node_id = PhysicalNode._latest_physical_node_id


class Server(PhysicalNode):
    _latest_server_id = 0

    def __init__(self):
        super().__init__()
        Server._latest_server_id += 1
        self.server_id = Server._latest_server_id


class Router(PhysicalNode):
    _latest_router_id = 0

    def __init__(self):
        super().__init__()
        Router._latest_router_id += 1
        self.router_id = Router._latest_router_id


class Switch(PhysicalNode):
    _latest_switch_id = 0

    def __init__(self):
        super().__init__()
        Switch._latest_switch_id += 1
        self.switch_id = Switch._latest_switch_id


class VirtualNode(Node, ABC):
    _latest_virtual_node_id = 0

    def __init__(self):
        super().__init__()
        VirtualNode._latest_virtual_node_id += 1
        self.virtual_node_id = VirtualNode._latest_virtual_node_id


class VirtualMachine(VirtualNode):
    _latest_virtual_machine_id = 0

    def __init__(self):
        super().__init__()
        VirtualMachine._latest_virtual_machine_id += 1
        self.virtual_machine_id = VirtualMachine._latest_virtual_machine_id


class Container(VirtualNode):
    _latest_container_id = 0

    def __init__(self):
        super().__init__()
        Container._latest_container_id += 1
        self.container_id = Container._latest_container_id


class VirtualRouter(VirtualNode):
    _latest_virtual_router_id = 0

    def __init__(self):
        super().__init__()
        VirtualRouter._latest_virtual_router_id += 1
        self.virtual_router_id = VirtualRouter._latest_virtual_router_id


class VirtualSwitch(VirtualNode):
    _latest_virtual_switch_id = 0

    def __init__(self):
        super().__init__()
        VirtualSwitch._latest_virtual_switch_id += 1
        self.virtual_switch_id = VirtualSwitch._latest_virtual_switch_id
