# Задание 1: Конвертер регистров

def convert_case(s: str, force: str = None) -> str:
    if force == 'snake' or (force is None and not '_' in s):
        # PascalCase -> snake_case
        result = ''
        for i, char in enumerate(s):
            if char.isupper() and i != 0:
                result += '_'
            result += char.lower()
        return result
    elif force == 'pascal' or (force is None and '_' in s):
        return ''.join(word.capitalize() for word in s.split('_'))
    else:
        return s

# Примеры:
print(convert_case('otus_course'))
print(convert_case('PythonIsTheBest'))
print(convert_case('python_is_the_best'))
print(convert_case('SuperValue', 'snake'))
print(convert_case('super_value', 'pascal'))

# -------------------------------------------------

# Задание 2: Проверка валидности даты

def is_valid_date(date_str: str) -> bool:
    from datetime import datetime
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False

# Примеры:
print(is_valid_date('29.02.2000'))
print(is_valid_date('29.02.2001'))
print(is_valid_date('31.04.1962'))

# -------------------------------------------------

# Задание 3: Проверка на простое число

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Примеры:
print(is_prime(17))
print(is_prime(20))
print(is_prime(23))

# -------------------------------------------------

# Задание 4: Учёт пользователей

def add_user(users: dict) -> None:
    while True:
        name = input('Имя: ').strip()
        if not name:
            break
        surname = input('Фамилия: ').strip()
        if not surname:
            break
        age_str = input('Возраст: ').strip()
        if not age_str:
            break
        id_str = input('ID: ').strip()
        if not id_str:
            break

        if not name.isalpha():
            print('Имя должно состоять только из букв!')
            continue
        if not surname.isalpha():
            print('Фамилия должна состоять только из букв!')
            continue
        name = name.capitalize()
        surname = surname.capitalize()
        if not age_str.isdigit() or not (18 <= int(age_str) <= 60):
            print('Возраст должен быть числом от 18 до 60!')
            continue
        age = int(age_str)
        if not id_str.isdigit():
            print('ID должен быть целым числом!')
            continue
        id_full = id_str.zfill(8)
        if id_full in users:
            print('ID должен быть уникальным!')
            continue

        users[id_full] = (name, surname, age)
        print('Пользователь добавлен!\n')

def print_users_table(users: dict) -> None:
    print(f'{"ID":<10} {"Имя":<12} {"Фамилия":<12} {"Возраст":<8}')
    print('-' * 44)
    for user_id, (name, surname, age) in users.items():
        print(f'{user_id:<10} {name:<12} {surname:<12} {age:<8}')

users = {
    '00000001': ('Иван', 'Петров', 24),
    '00000002': ('Ольга', 'Сидорова', 36),
}
print_users_table(users)
