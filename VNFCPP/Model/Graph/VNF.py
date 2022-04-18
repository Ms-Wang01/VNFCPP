from VNFCPP.Model.Graph.Requirement import VNFRequirement


class VNF:
    _latest_vnf_id = 0

    def __init__(self, **kwargs):
        VNF._latest_vnf_id += 1
        self._vnf_id = VNF._latest_vnf_id
        self._vnf_name = kwargs["vnf_name"] if "vnf_name" in kwargs else None
        self._vnf_requirement = kwargs["vnf_requirement"] if "vnf_requirement" in kwargs else None
        self._vnf_host = kwargs["vnf_host"] if "vnf_host" in kwargs else None

    def __str__(self) -> str:
        return self._vnf_name

    @classmethod
    def get_number_of_vnfs(cls) -> int:
        return cls._latest_vnf_id

    @property
    def vnf_id(self) -> int:
        return self._vnf_id

    @property
    def vnf_name(self) -> str:
        return self._vnf_name

    @vnf_name.setter
    def vnf_name(self, value: str):
        self._vnf_name = value

    @property
    def vnf_requirement(self) -> VNFRequirement:
        return self._vnf_requirement

    @vnf_requirement.setter
    def vnf_requirement(self, value: VNFRequirement):
        self._vnf_requirement = value

    @property
    def vnf_host(self):
        return self._vnf_host

    @vnf_host.setter
    def vnf_host(self, value):
        self._vnf_host = value

    @vnf_host.deleter
    def vnf_host(self):
        del self._vnf_host
