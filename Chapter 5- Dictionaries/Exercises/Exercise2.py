'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

words = {'float': 'Decimal and Integers.', 'comment': 'A note in a program that the Python interpreter ignores.', 'print': 'Displays the specified message to the screen.', 'variable': 'a reserved memory location to store values.', 'dictionary': "A collection of key-value pairs."}

word = 'float'
print("\n" + word.title() + ": " + words[word])

word = 'comment'
print("\n" + word.title() + ": " + words[word])

word = 'print'
print("\n" + word.title() + ": " + words[word])

word = 'variable'
print("\n" + word.title() + ": " + words[word])

word = 'dictionary'
print("\n" + word.title() + ": " + words[word])
