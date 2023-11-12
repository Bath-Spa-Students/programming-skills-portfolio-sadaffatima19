'''Write a Python program to merge two dictionaries into one.'''

names = {1: "Asra", 2: "Azra", 3: "Marwa", 4: "Sadaf"}
friends = {5: "Rahma", 6: "Alia", 7: "Ammara"}
people = names | friends
print(people)
