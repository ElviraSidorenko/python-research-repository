# Returns a list of all primes up to a given number

def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor == 0:
                # Not prime
                break
            if factor > sqrtNum:
                # It's prime!
                primes.append(number)
                break
    return primes


# Get the input
upTo = int(input('Get prime numbers up to: '))

# Display result
print(allPrimesUpTo(upTo))
