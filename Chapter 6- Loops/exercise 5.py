#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ['catchy', 'sapino', 'freezeland', 'rejoice', 'smash wish', 'spicy club']
print("Sorry, we have run out of pastrami sandwiches.")
while 'freezeland' in sandwich_orders:
    sandwich_orders.remove('freezeland')
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making {current_sandwich} sandwich...")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
