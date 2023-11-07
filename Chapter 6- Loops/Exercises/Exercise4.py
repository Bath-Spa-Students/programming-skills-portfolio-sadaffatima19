'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

sandwich_orders = ["Egg Sandwich", "Chicken Sandwich", "Cheese Sandwich", "Club Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    print("I'm preparing your " + new_sandwich)
    finished_sandwiches.append(new_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich)
