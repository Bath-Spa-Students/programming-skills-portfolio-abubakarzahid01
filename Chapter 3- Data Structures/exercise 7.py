#Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.
#•	 Show that your list is still in its original order by printing it.
#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#•	 Show that your list is still in its original order by printing it again.
#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
# list of Places to visit.
places_to_visit = ["turkey", "dubai", "New York", "india", "islamabad"]
# Print the list as it is.
print("Original Order: ", places_to_visit)
#Use sorted() to print the list in alphabetical order without changing the list itself.
print("Alphabetical Order: ", sorted(places_to_visit))
#Print the list to prove that it remains in order.
print("Original Order: ", places_to_visit)
#print sorted(list,reverse)
print("Reverse Alphabetical Order: ", sorted(places_to_visit, reverse=True))
#Then, print the list to proof that its order has remained original.
print("Original Order: ", places_to_visit)
#reverse() = # Reverse the order of the list
places_to_visit.reverse()
# Print the list to show its order has changed
print("Reversed Order: ", places_to_visit)
#reverse(reverse(list))
places_to_visit.reverse()
# Let’s print it to prove that it’s okay!
print("Original Order: ", places_to_visit)
#sort().
places_to_visit.sort()
# Print the list to show its order has changed
print("Alphabetical Order: ", places_to_visit)
#sort(list.sort(reverse=True))
places_to_visit.sort(reverse=True)
# Print the list to indicate its order changed.
print("Reverse Alphabetical Order: ", places_to_visit)

