S = "spam"
print(S[0][0][0][0][0])
my_list = ['s', 'p', 'a', 'm']
try:
    print(my_list[0][0][0][0][0])
except TypeError as e:
    print(f"Ошибка: {e}")
