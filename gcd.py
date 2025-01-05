

def gcd(a, b):
    while b:
        a, b = b, a % b
        print(f'a={a} b={b}')


    print(f'result={a}')
    return a


gcd(115, 25)

