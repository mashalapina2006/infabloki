S = "spam"
S = 's' + 'l' + S[2:]  
print(S) 
S = S[0].replace('p', 'l') + S[1:].replace('p', 'l') 
print(S)
try:
    S[1] = 'l'  
except TypeError as e:
    print(f"Ошибка: {e}")
