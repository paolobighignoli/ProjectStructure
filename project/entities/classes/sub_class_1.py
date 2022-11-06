from project.entities.classes.abstract_class import AbstractClass
from typing import *


class SubClass(AbstractClass):

    def first_method(self, arg_1: float, arg_3: List[int]) -> List[str]:
        new_list = []
        for arg in arg_3:
            new_list.append(str(arg_1*arg))
        return new_list

    def another_method(self, arg_1: str, arg_2: int) -> Dict[str, int]:
        
        return {arg_1: arg_2}
