#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#•Write one version of this program that runs the if block and another that runs the else block.
# If block 
alien_colour = 'green'
if alien_colour == 'green':
    print("The player just earned 5 points for shooting the alien.")
    # Else block
    alien_colour = 'red'
    if alien_colour == 'green':
        print("The player just earned 5 points for shooting the alien.")
    else:
        print("The player just earned 10 points.")
