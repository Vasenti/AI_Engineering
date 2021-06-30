def get_prime_numbers(number):
    prime_numbers = []
    for i in range(1, (number + 1)):
        count = 0
        for e in range(1, (number + 1)):
            if i % e == 0:
                count += 1
        if count == 2:
            prime_numbers.append(i)
    return prime_numbers

print(str(get_prime_numbers(76)))