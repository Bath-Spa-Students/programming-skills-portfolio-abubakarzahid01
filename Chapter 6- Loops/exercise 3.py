#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
counter = 0
while True:
    counter += 1
    if counter % 2 == 0:
        print("Even number:", counter)
    else:
        print("odd number:, counter")