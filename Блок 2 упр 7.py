try:
    print("hello" + [1, 2, 3]) 
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print([1, 2] + (3, 4))  
except TypeError as e:
    print(f"Ошибка: {e}")


try:
    print([1, 2] + {'a': 1, 'b': 2})  
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    print("hello" + {'a': 1, 'b': 2})  
except TypeError as e:
    print(f"Ошибка: {e}")


my_list = [1, 2, 3]
my_list.append(4)
print(f"Список после append: {my_list}")

my_string = "hello"
try:
    my_string.append(" world")
except AttributeError as e:
    print(f"Ошибка: {e}")

try:
    my_list.keys()
except AttributeError as e:
    print(f"Ошибка: {e}")


list1 = [1, 2, 3]
list2 = list1[1:]  
print(f"Тип list2 (нарезание): {type(list2)}")

list3 = list1 + [4, 5]  
print(f"Тип list3 (конкатенация списков): {type(list3)}")

string1 = "hello"
string2 = string1[1:]  
print(f"Тип string2 (нарезание): {type(string2)}")

string3 = string1 + " world"  
print(f"Тип string3 (конкатенация строк): {type(string3)}")
