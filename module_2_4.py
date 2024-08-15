numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        print(n , " - не подходящее число")
    else:
        for j in range(2, int(n+1)):
            if n % j == 0 and n != j:
                is_prime = False
                break
        if is_prime == True:
            primes.append(n)
        else:
            not_primes.append(n)
print("простые числа: ", primes)
print("Составные числа: ", not_primes)


