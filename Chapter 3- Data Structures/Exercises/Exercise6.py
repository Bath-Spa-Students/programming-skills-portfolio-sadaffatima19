members = ["Rahma", "Alia", "Ammara"]
print(f"Since you're always hungry, I want to invite you for dinner. Please come {members[0]}.")
print(f"I made your favorite meal for dinner. Please come {members[1]}.")
print(f"If you want to have the most delicious dinner tonight. Please come {members[2]}.")
print(f"{members[2]} can't make it tonight for dinner")
members[2] = "Angel"
print(members)
print(f"Since you're always hungry, I want to invite you for dinner. Please come {members[0]}.")
print(f"I made your favorite meal for dinner. Please come {members[1]}.")
print(f"If you want to have the most delicious dinner tonight. Please come {members[2]}.")
print("My dinner table won't be arriving in time for the dinner, so I will be able to invite onlly two people.")
name = members.pop(2)
print(f"{name}, I'm sorry, but I won't be able to invite you for dinner.")
print(f"Hi {members[0]}. You're still invited to the dinner.")
print(f"Hi {members[1]}. You're still invited to the dinner.")
del members[0]
del members[0]
print(members)