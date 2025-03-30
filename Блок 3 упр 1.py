S = "Hello, World!"

# а) 
for char in S:
    print("Символ: " + char + ", Код ASCII: " + str(ord(char)))

# б) 
ascii_sum = 0
for char in S:
    ascii_sum += ord(char)
print("Сумма кодов ASCII: " + str(ascii_sum))

# в) 
ascii_codes = [ord(char) for char in S]
print("Список кодов ASCII: " + str(ascii_codes))

# Сравнение с map
ascii_codes_map = list(map(ord, S))
print("Список кодов ASCII с использованием map: " + str(ascii_codes_map))
