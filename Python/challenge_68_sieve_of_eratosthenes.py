"""
Challenge 68: Mathematical Challenge - Sieve of Eratosthenes

Problem Statement:
Implement the Sieve of Eratosthenes algorithm to efficiently find all prime
numbers up to a given integer `n`.

Algorithm Steps:
1. Create a boolean list `is_prime` of size `n + 1` and initialize all
   entries to `True`. `is_prime[i]` will be `False` if `i` is not a prime.
2. Mark 0 and 1 as not prime (`False`).
3. Loop from `p = 2` up to the square root of `n`.
4. If `is_prime[p]` is still `True`, then `p` is a prime number.
5. For this prime `p`, iterate through its multiples (starting from `p*p`)
   and mark them as not prime (`False`).
6. After the loop, all indices `i` for which `is_prime[i]` is `True` are the
   prime numbers.

Solution:
"""
import math

def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Finds all prime numbers up to n using the Sieve of Eratosthenes.
    
    Args:
        n: The upper limit to search for primes.
        
    Returns:
        A list of all prime numbers from 2 to n.
    """
    if n < 2:
        return []
        
    # 1. Create a boolean list to mark numbers as prime or not.
    is_prime = [True] * (n + 1)
    
    # 2. Mark 0 and 1 as not prime.
    is_prime[0] = is_prime[1] = False
    
    # 3. Loop from 2 up to sqrt(n).
    for p in range(2, int(math.sqrt(n)) + 1):
        # 4. If p is a prime number...
        if is_prime[p]:
            # 5. ...mark all of its multiples as not prime.
            # We can start from p*p because smaller multiples
            # would have been marked by smaller primes.
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    # 6. Collect all the numbers that are still marked as prime.
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes

# Example usage:
if __name__ == "__main__":
    upper_limit = 100
    prime_numbers = sieve_of_eratosthenes(upper_limit)
    
    print(f"Prime numbers up to {upper_limit}:")
    print(prime_numbers)
    
    upper_limit_2 = 29
    prime_numbers_2 = sieve_of_eratosthenes(upper_limit_2)
    print(f"\nPrime numbers up to {upper_limit_2}:")
    print(prime_numbers_2)

"""
Expected Output:

Prime numbers up to 100:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

Prime numbers up to 29:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
""" 