from abc import ABC, abstractmethod
from typing import *


class AbstractClass(ABC):

    @abstractmethod
    def first_method(self, arg_1: float, arg_2: float,
                         arg_3: List[int]) -> List[str]:
        """
        Description of first_method
        """
        raise NotImplementedError()

