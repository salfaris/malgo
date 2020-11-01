from typing import Callable

class OneParamRangeTest:
    """Test 1-parameter functions over a range of integers."""
    def __init__(self, range: int = None):
        self.range = 13 if range is None else range

    def set_func(self, func: Callable):
        self.func = func
    
    def generate(self, func: Callable) -> None:
        self.set_func(func)
        for i in range(1, self.range):
            self.nice_print(i)

    def nice_print(self, param: int) -> None:
        if param < 10:
            print(f"n = {param}   | f({param}) = {self.func(param)}")
        else:
            print(f"n = {param}  | f({param}) = {self.func(param)}")

# class TwoParamRangeTest(OneParamRangeTest):
#     def __init__(self, range: int = None):
#         super.__init__(range)
    
#     def two_param_generate(self, func: Callable) -> None:
#         self.set_func(func)
#         for i in range(1, self.range):
#             self.nice_print(i)
            
#     def nice_print(self, param:)