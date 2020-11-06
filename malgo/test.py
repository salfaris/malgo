import numpy as np
from typing import Callable

class OneParamRangeTest:
    """Test 1-parameter functions over a range of integers."""
    def __init__(self, range: int = None):
        self.range = 13 if range is None else range

    def set_func(self, func: Callable):
        """We expect the parameter of `func` to be the number range."""
        self.func = func
    
    def generate(self, func: Callable) -> None:
        self.set_func(func)
        for i in range(1, self.range):
            self.nice_print(i)

    def nice_print(self, param: int) -> None:
        evaluated_func = self.func(param)
        if param < 10:
            print(f"n = {param}   | f({param}) = {evaluated_func}")
        else:
            print(f"n = {param}  | f({param}) = {evaluated_func}")

class TwoParamRangeTest(OneParamRangeTest):
    def __init__(self, range: int = None):
        super().__init__(range)
            
    def set_param_two(self, param2: int):
        self.param_two = param2
        return self
    
    def nice_print(self, param: int) -> None:
        evaluated_func = self.func(param, self.param_two)
        if param < 10:
            print(f"n = {param}   | f({param}) = {evaluated_func}")
        else:
            print(f"n = {param}  | f({param}) = {evaluated_func}")

class FunctionTest:
    """Test algorithm on a family of functions."""
    def __init__(self):
        # self.func = lambda x: x if func is None else func
        self.function_list = [
            lambda x: x,
            lambda x: x + 2,
            lambda x: x**2 + 3,
            lambda x: 2 / (x**2+1),
            np.sin
        ]
    
    def get_functions(self):
        return self.function_list
      
    # def init_test(self, algo: Callable) -> None:
    #     for func in self.function_list: