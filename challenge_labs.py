# Creating a function that checks if the value is a prime umber or not
def check_prime(number):
    half = number // 2
    for i in range(2, half):
        if number % i == 0:
            return False
    return True


def check_list(values):
    primes = []
    for val in values:
        if val % 2 == 0 or val % 3 == 0:
            continue
        elif val in [2, 3]:
            result = True
        else:
            result = check_prime(val)
        if result is True:
            primes.append(val)
    return primes



# Saving the prime numbers to a file
with open('results.txt', 'w+') as file:
    for numb in check_list(range(2, 251)):
        file.write(str(numb) + "\n")
