'''Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
•If the aliens color is green, print a statement that the player just earned 5 points for shooting the alien.
•If the aliens color isnt green, print a statement that the player just earned 10 points.
•Write one version of this program that runs the if block and another that runs the else block.'''

#if block
alien_color = "Green"
if alien_color == "Green":
    print("You have earned 5 points for shooting the alien!")
else:
    print("You have earned 10 points.")

#else block
alien_color = "Red"
if alien_color == "Green":
    print("You have earned 5 points for shooting the alien!")
else:
    print("You have earned 10 points.")
