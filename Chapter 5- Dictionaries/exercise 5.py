#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet
pets = [
    {"animal": "dog", "owner": "adil"},
    {"animal": "cat", "owner": "rsahid"},
    {"animal": "bird", "owner": "faisal"}   
]
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()

