from abc import ABC, abstractmethod


class Specs:
    def __init__(self, **kwargs) -> None:
        self._cpu = kwargs["cpu"] if "cpu" in kwargs else None
        self._memory = kwargs["memory"] if "memory" in kwargs else None
        self.storage = kwargs["storage"] if "storage" in kwargs else None

    @property
    def cpu(self) -> int:
        return self._cpu

    @cpu.setter
    def cpu(self, value: int):
        self._cpu = value

    @cpu.deleter
    def cpu(self):
        del self._cpu

    @property
    def memory(self) -> int:
        return self._memory

    @memory.setter
    def memory(self, value: int):
        self._memory = value

    @memory.deleter
    def memory(self):
        del self._memory

    @property
    def storage(self) -> int:
        return self._storage

    @storage.setter
    def storage(self, value: int):
        self._storage = value

    @storage.deleter
    def storage(self):
        del self._storage


class CompRequirement(ABC):
    def __init__(self, **kwargs) -> None:
        self._specs = kwargs["specs"] if "specs" in kwargs else None

    @property
    def specs(self) -> Specs:
        return self._specs

    @specs.setter
    def specs(self, value: Specs):
        self._specs = value

    @specs.deleter
    def specs(self):
        del self._specs


class LinkRequirement:

    def __init__(self, **kwargs) -> None:
        self._propagation_delay = kwargs["propagation_delay"] if "propagation_delay" in kwargs else None
        self._bandwidth = kwargs["bandwidth"] if "bandwidth" in kwargs else None

    @property
    def propagation_delay(self) -> float:
        return self._propagation_delay

    @propagation_delay.setter
    def propagation_delay(self, value: float):
        self._propagation_delay = value

    @property
    def bandwidth(self) -> float:
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value: float):
        self._bandwidth = value


class VNFRequirement(CompRequirement):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._processing_delay = kwargs["processing_delay"] if "processing_delay" in kwargs else None

    @property
    def processing_delay(self) -> float:
        return self._processing_delay

    @processing_delay.setter
    def processing_delay(self, value: float):
        self._processing_delay = value

    @processing_delay.deleter
    def processing_delay(self):
        del self._processing_delay


class SCRequirement(CompRequirement):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._e2e_delay = kwargs["e2e_delay"] if "e2e_delay" in kwargs else None

    @property
    def e2e_delay(self) -> float:
        return self._e2e_delay

    @e2e_delay.setter
    def e2e_delay(self, value: float):
        self._e2e_delay = value

    @e2e_delay.deleter
    def e2e_delay(self):
        del self._e2e_delay
