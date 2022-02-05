bloods = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

result = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}

for blood in bloods:
    if blood == "A":
        result['A'] += 1
    elif blood == "O":
        result['O'] += 1
    elif blood == "B":
        result['B'] += 1
    elif blood == "AB":
        result['AB'] += 1
        
print(result)

print(result['AB'])
