import sys

"""List of primes that we have seen"""
primes = [2]

def generate(num):
    """Returns the list of prime factors for the given argument
    
    Arguments:
    - `num`: Integer
    Returns:
    List of prime factors of num
    """

    factors = []
    if num < 2:
        return factors
    loop = 2
    while loop < num:
        if num % loop == 0 and is_prime(loop):
            while(num % loop == 0):
                num /= loop
                factors.append(loop)
        loop = loop + 1
    factors.sort()
    
    return factors

def is_prime(n):
    """
    Checks whether the given number is a prime
    """
    if n in primes:
        return 1
    if n % 2 == 0:
        return 0
    for i in range(3, n//2 + 1, 2):
        if n % i == 0:
            return 0
    primes.append(n)
    return 1

if __name__ == '__main__':
    print(generate(sys.maxsize))
