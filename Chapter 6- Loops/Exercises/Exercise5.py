'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to 
print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.'''

sandwich_orders = ["Pastrami Sandwich", "Egg Sandwich", "Pastrami Sandwich", "Chicken Sandwich", "Cheese Sandwich", "Pastrami Sandwich", "Club Sandwich"]
finished_sandwiches = []

print("I'm sorry, we're out of Pastrami Sandwich.")
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

print("\n")
while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    print("I'm preparing your " + new_sandwich)
    finished_sandwiches.append(new_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich)
