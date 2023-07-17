import abc
from typing import Dict, Tuple, List, Hashable, Any
import scipy.sparse as sp
import numpy as np
import numpy.typing as npt


class TransformGraphBase(abc.ABC):
    strict_check: bool
    check: bool
    nodes: List[Hashable]
    i: List[int]
    j: List[int]
    transform_to_ij_index = Dict[Tuple[Hashable, Hashable], int]
    connections: sp.csr_matrix
    dist: np.ndarray
    predecessors: np.ndarray
    _cached_shortest_paths: Dict[Tuple[int, int], List[Hashable]]
    _transforms = Dict[Tuple[Hashable, Hashable], Any]

    def __init__(self, strict_check: bool = ...,
                 check: bool = ...) -> "TransformGraphBase": ...

    @property
    @abc.abstractmethod
    def transforms(self) -> Dict[Tuple[Hashable, Hashable], Any]: ...

    @abc.abstractmethod
    def _transform_available(self, key: Tuple[Hashable, Hashable]) -> bool: ...

    @abc.abstractmethod
    def _set_transform(self, key: Tuple[Hashable, Hashable], A2B: Any): ...

    @abc.abstractmethod
    def _get_transform(self, key: Tuple[Hashable, Hashable]) -> Any: ...

    @abc.abstractmethod
    def _del_transform(self, key: Tuple[Hashable, Hashable]): ...

    def has_frame(self, frame: Hashable) -> bool: ...

    def _invert_transform(self, A2B_matrix: np.ndarray) -> np.ndarray: ...

    def _check_transform(self, A2B_matrix: np.ndarray) -> np.ndarray: ...

    def add_transform(self, from_frame: Hashable, to_frame: Hashable,
                      A2B: Any) -> "TransformGraphBase": ...

    def _recompute_shortest_path(self): ...

    def remove_transform(
            self, from_frame: Hashable,
            to_frame: Hashable) -> "TransformGraphBase": ...

    def _shortest_path(self, i: int, j: int) -> List[Hashable]: ...

    def connected_components(self) -> int: ...

    def check_consistency(self) -> bool: ...
