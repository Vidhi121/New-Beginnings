"""
Sieve of Eratosthenes is used to find prime numbers. Following code takes limit till which we have to find
a prime number. Marks all composite as <not prime>."""

def sieve(n):
    prim = [False] * 2 + [True] * (n - 1) 
    for i in xrange(int(n**0.5 + 1.5)): 
        if prim[i]:
            for j in xrange(i*i, n+1, i):
                prim[j] = False
    return [i for i, prime in enumerate(prim) if prime]

def main():
    try:
        n = int(raw_input('Enter a number: '))
        print sieve(n)
    except ValueError:
        print 'Enter only an integer value, n > 1.'
        main()
        
if __name__ == '__main__':
    main()
