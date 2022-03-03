T=input()
if T.isupper():
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(T, ord(T), T.lower(), ord(T.lower())))
elif T.islower():
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(T, ord(T), T.upper(), ord(T.upper())))
    
    
#ord(문자) ->해당 아스키코드 숫자 
#chr(숫자) ->해당 아스키코드 문자