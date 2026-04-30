import random
from typing import List

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes(count: int) -> List[int]:
    result = []
    num = 2
    while len(result) < count:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

def checksum(x: List[int]) -> int:
    cs = 0
    for val in x:
        cs = ((cs + val) * 113) % 10_000_007
    return cs

def pipeline(count: int = 1000, seed: int = 100) -> int:
    p_list = primes(count)
    random.seed(seed)
    random.shuffle(p_list)
    return checksum(p_list)

if __name__ == "__main__":
    print(pipeline())
