# Домашнее задание: Базовые типы данных (неизменяемые)

# Задание 1: Зеркальное отражение цифр
num = input("Введите пятизначное число: ")
print(num[0] + num[3] + num[2] + num[1] + num[4])

# Задание 2: Подсчет выходных до отпуска
days = int(input("Сколько дней до отпуска? "))
weekends = days // 7 * 2 + (days % 7 + 1) // 6
print(weekends)

# Задание 3: Плитка шоколада
a = int(input("Длина плитки: "))
b = int(input("Ширина плитки: "))
k = int(input("Размер куска: "))
print(((k % a == 0) + (k % b == 0)) > 0 and k < a * b)

# Задание 4: Римские числа (до 3999)
n = int(input("Введите целое число для преобразования в римское: "))
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
roman = ""
i = 0
while n > 0:
    count = n // values[i]
    roman += letters[i] * count
    n -= values[i] * count
    i += 1
print(roman)

# Задание 5: Проверка на вещественное положительное число
s = input("Введите данные: ")
dot_count = s.count('.')
only_digits_and_dot = s.replace('.', '', 1).isdigit()
is_positive = s.replace('.', '', 1).replace('0', '') != '-' * (s.startswith('-'))
print(dot_count <= 1 and only_digits_and_dot and not s.startswith('-') and s != ".")