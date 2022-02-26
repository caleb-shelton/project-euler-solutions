import math


def check_prime(n):
    if n < 2:
        return False
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


num = 600851475143
for i in range(round(math.sqrt(num)), 1, -1):
    if (num / i) % 1 == 0 and check_prime(i):
        print(i)
        break
