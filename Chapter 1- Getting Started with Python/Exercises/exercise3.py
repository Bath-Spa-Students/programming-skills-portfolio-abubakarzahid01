import datetime 
current_datetime = datetime.datetime.now()
formate_datetime = current_datetime.strftime("%d %b %Y %I %M %p")
print("Current date and time:", formate_datetime)