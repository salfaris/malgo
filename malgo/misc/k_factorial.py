# System imports
import sys
sys.path.append('.')

from malgo.test import OneParamRangeTest, TwoParamRangeTest

def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
def double_factorial(n: int):
    return 1 if n < 2 else n*double_factorial(n-2)

def triple_factorial(n: int):
    return 1 if n < 3 else n*triple_factorial(n-3)

def k_factorial(n: int, k: int):
    return 1 if n < k else n*k_factorial(n-k, k)


# TESTS GOES HERE
if __name__ == '__main__':
    print("Factorial Test")
    OneParamRangeTest().generate(triple_factorial)
    TwoParamRangeTest().set_param_two(3).generate(k_factorial)