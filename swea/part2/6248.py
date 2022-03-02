chars = input()

result = ''
for i in range(0,len(chars)+1, 2):
    result += chars[i]

print(result)