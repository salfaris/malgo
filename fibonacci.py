from test import OneParamRangeTest

def fibonacci_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_num(n-1) + fibonacci_num(n-2)

def modified_fibo_num(n):
    if n < 3:
        return 1
    else:
        return (modified_fibo_num(n-1) + modified_fibo_num(n-2) 
                + modified_fibo_num(n-3))


# Test here
if __name__ == '__main__':
    print("Fibonacci Test")
    OneParamRangeTest().generate(fibonacci_num)