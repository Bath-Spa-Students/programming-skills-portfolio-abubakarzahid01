#Write a Python program that uses the break statement to exit a for loop when a specific
#condition is met.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
    print("loop ended")