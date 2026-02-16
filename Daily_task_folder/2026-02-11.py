def is_prime_or_not(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return False
    else:
        for i in range(2, n, +1):
            if n % i == 0:
                return False
        return True
    
