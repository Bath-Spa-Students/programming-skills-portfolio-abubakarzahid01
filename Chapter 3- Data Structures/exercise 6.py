#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
guests = ['soban', 'usman', 'adil', 'rsahid', 'faisal']
print("I can only invite two people for dinner.")
while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry {guest}, I can't invite you to dinner.")
    print(f"{guest[0]} and {guest[1]}, you're still invited to dinner.")
    del guests[0]
    del guests[0]
    print(guests)