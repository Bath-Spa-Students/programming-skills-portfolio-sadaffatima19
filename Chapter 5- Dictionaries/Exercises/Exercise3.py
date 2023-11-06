'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms
to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.'''

glossary = {'Indentation': 'Indentation refers to the spaces at the beginning of a code line.', 'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.', 'Int': 'The integer number type.',
    'dictionary': "A collection of key-value pairs.", 'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.', 'Boolean Values': 'True or False.',
    'float': 'A numerical value with a decimal component.', 'Operators': 'Use operator to perform operations in Python.',}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
