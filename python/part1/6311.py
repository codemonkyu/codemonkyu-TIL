a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

list_a = list(a)
count = 0

for i in list_a:
    if i == "A":
        count += 4
    elif i == "B":
        count += 3
    elif i == "C":
        count += 2
    elif i == "D":
        count += 1
    
print(count)