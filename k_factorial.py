def main():
    k = 2
    fact_mark = make_fact_mark(k)
    for i in range(1, 13):
        if i < 10:
            print(f"n = {i}  | {i}{fact_mark} = {k_factorial(i, k)}")
        else:
            print(f"n = {i} | {i}{fact_mark} = {k_factorial(i, k)}")

def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

def double_factorial(n: int):
    return 1 if n < 2 else n*double_factorial(n-2)

def triple_factorial(n: int):
    return 1 if n < 3 else n*triple_factorial(n-3)

def k_factorial(n: int, k: int):
    return 1 if n < k else n*k_factorial(n-k, k)

def make_fact_mark(k):
    mark = ""
    for _ in range(k):
        mark += "!"
    return mark


if __name__ == '__main__':
    main()