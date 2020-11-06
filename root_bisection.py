from custom_type import Function, Real

def bisection(f: Function, a: Real, b: Real):
    tol = 1/10 ** 10
    step = 0
    while True:
        c = float(a+b) / 2  # Compute c
        if abs(f(c)) < tol:
            step += 1
            print(f"Found zero at x = {c}; after {step} step(s).")
            return c
        elif f(a)*f(c) < 0:
            step += 1
            b = c
        elif f(b)*f(c) < 0:
            step += 1
            a = c
        else:
            return  # Bad exit.
        print(f"Interval: [{a}, {b}]")


# # TEST CASE
# if __name__ == '__main__':
#     # f = lambda x: x**3 - 3*x + 4
#     f = lambda x: x**2 - 3*x - 1

#     for method in [bisection]:
#         method(f, -4, 4)
#         # res = method(f, -4, 4)
#         # print(res)
#         # print(f(res))
    