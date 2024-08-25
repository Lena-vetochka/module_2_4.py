numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i <= 1:
        numbers.remove(i)
        for j in numbers:
            if j == 2 or j == 3:
                primes.append(j)
            elif j % 2 == 0 or j % 3 == 0:
                    not_primes.append(j)
            else:
                primes.append(j)
print(primes)
print(not_primes)
