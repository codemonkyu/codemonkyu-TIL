url = list(input().split('/'))

url_temp = []
for i in url:
    if i:
        url_temp.append(i)
        
print(f'protocol: {url_temp[0][:-1]}')
print(f'host: {url_temp[1]}')
print(f'others: {url_temp[2]}')

