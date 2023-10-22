#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#*Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.
#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
glossary = {
    'variable': 'A named location in memory used to store a value.',
    'function': 'A block of organized, resusable code that performs a specific task.',
    'loop': 'A  programming construct that repeats a group of commands.',
    'loop': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.'
}
for key, value in glossary.items():
    print(f"{key}: {value}\n")