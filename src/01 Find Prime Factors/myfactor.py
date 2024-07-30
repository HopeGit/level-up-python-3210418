# def prime_factors(number):
#    factors = []
#    divisor = 2
#    while divisor <= number:
#        if number % divisor == 0:
#            factors.append(divisor)
#            number = number // divisor
#        else:
#            divisor += 1
#    return factors
#

# commands used in solution video for reference
#if __name__ == '__main__':
#    print(prime_factors(630))  # [2, 3, 3, 5, 7]
#    print(prime_factors(13))  # [13]



def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes
    
def getFactors(n):
    return [factor for factor in range(1, n+1) if n % factor == 0]

#    print(getfactors(630))  # [2, 3, 3, 5, 7]
#    print(getfactors(13))  # [13]

# print(listPrimes(100))

print(listPrimes(630))
