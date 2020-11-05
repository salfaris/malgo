from typing import List, Any
from custom_type import Function, Real, KernelMethod

class IntegralKernel:
    def __init__(self, func: Function, startpoint: Real, endpoint: Real):
        self.func = func
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.subdivisions = 50
        self.methods = []
    
    def add_method(self, methods: List[KernelMethod]):
        self.methods.extend(methods)
        self.methods = list(set(self.methods))
        return self
    
    def integrate(self, method: KernelMethod, subdivisions: int = None):
        if subdivisions is None:
            res = method(self.func,
                         self.startpoint,
                         self.endpoint,
                         self.subdivisions)
        else:
            res = method(self.func,
                         self.startpoint,
                         self.endpoint,
                         subdivisions)
        return res
    
    def integrate_pretty(self, subdivisions: int = None):
        table_header = ['method', 'return']
        col_method = [method.__name__ for method in self.methods]
        
        if subdivisions is None:
            col_return = [self.integrate(method) for method in self.methods]
        else:
            col_return = [(self.integrate(method, subdivisions) 
                           for method in self.methods)]
            
        generate_table(table_header, col_method, col_return)
        return self
    
class NotMatchError(Exception):
    pass

def generate_table(header: List[str], *columns: List[Any]):
    """Code credit: https://stackoverflow.com/a/39032993/13698939"""
    
    if len(header) != len(columns):
        msg = "Expect column header to match number of columns."
        raise NotMatchError(msg)
    
    table_data = [header] + list(zip(*columns))
    
    # Begin printing the table
    for idx, row in enumerate(table_data):
        line = '|'.join(str(x).ljust(12) for x in row)
        print(line)
        if not idx:
            print('-' * len(line))