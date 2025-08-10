def isPrime(n):
    if n <= 0:
        return False
    for x in range(2,n//2):
        if n % 2 == 0:
            return False
    return True


print(isPrime(15))
