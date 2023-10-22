#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
glossary = { 
    'variable': 'set point for value', 
    'string': 'character', 
    'list': 'Collection of primary sequence', 
    'tuple': 'Immutable Character', 
    'Dictionary': 'Collection of key-value pairs', 
} 
for key,value in glossary.items():
    print(f"{key.title()}: {value}")
    
glossary['loop'] = 'A method to iterate through collections'
glossary['function'] = 'A piece of code that performs a specific function'
glossary['class'] = 'Creative design'
glossary['module'] = 'File containing Python code'
glossary['package'] = 'Package module'
print(glossary)