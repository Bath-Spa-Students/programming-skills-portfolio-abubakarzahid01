#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.
while True:
    topping = input("Enter a pizza topping (enter 'quit' to exits): ")
    if topping == 'quit':
        break
print(f"I'll add {topping} to your pizza!")
