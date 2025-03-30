person = {
    'name': {
        'first': 'Мария',
        'middle': 'Денисовна',
        'last': 'Лапина'
    },
    'age': 19,
    'job': 'Лингвист',
    'address': {
        'street': 'ул. площадь Ленина, 10',
        'city': 'Воронеж',
        'zip': '123456'
    },
    'email': 'marylapina01@yandex.ru',
    'phone': '+7 (000) 000 00 00'
}

print(f"Имя: {person['name']['first']}")
print(f"Отчество: {person['name']['middle']}")
print(f"Фамилия: {person['name']['last']}")
print(f"Возраст: {person['age']}")
print(f"Место работы: {person['job']}")
print(f"Адрес: {person['address']['street']}, {person['address']['city']}")
print(f"Email: {person['email']}")
print(f"Телефон: {person['phone']}")
