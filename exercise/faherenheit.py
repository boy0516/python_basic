def c_to_f(n1):
    a = ((9 / 5) * n1) + 32
    return a

def sayhello(msg):
    return f'Hello{msg}'

c1 = float(input())

print(round(c_to_f(c1), 2))

print('{:.2f}'.format(c_to_f(c1)))