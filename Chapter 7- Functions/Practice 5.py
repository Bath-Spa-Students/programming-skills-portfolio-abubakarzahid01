#Write a Python program that defines a function to check whether a given number is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(7)) #output: true
print(is_prime(10)) #output: false