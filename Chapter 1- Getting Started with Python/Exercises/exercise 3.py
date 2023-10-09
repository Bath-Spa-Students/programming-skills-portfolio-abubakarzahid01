# Exercise 3: Print date and Time :ballot_box_with_check:
import datetime 
current_datetime = datetime.datetime.now()
formate_datetime = current_datetime.strftime("%d %b %Y %I %M %p")
print("Current date and time:", formate_datetime)