def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numberRange(lower, higher):
    primes = []
    for num in range(lower, higher + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print(numberRange(10, 100))