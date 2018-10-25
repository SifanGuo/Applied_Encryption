# this script will cover the most computationally efficient
# method for fast-powering

def fast_power(g, A, N):
    a = g
    b = 1
    while A > 0:
        if A % 2 == 1:
            b = (b*a)% N
            a = (a**2) % N
        A //= 2

    return b


print(fast_power(7814, 26714, 27077))
