#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.
usb_price = 6
budget = 50
num_usb = budget // usb_price 
leftover = budget % usb_price 
print("Number of USB stick:",num_usb)
print("Pounds leftover:",leftover)