# --- Задание 1: Получение однозначного числа ---

def single_digit_sum(num):
    num = abs(num)
    while num > 9:
        num = sum(map(int, str(num)))
    return num

print("Задание 1: Получение однозначного числа")
n = int(input("Введите целое число: "))
print("Результат:", single_digit_sum(n))


# --- Задание 2: Кинотеатр ---

def find_row(seats, k):
    for i, row in enumerate(seats):
        count = 0
        for j in range(len(row)):
            if row[j] == 0:
                count += 1
                if count == k:
                    # Проверяем последние k мест подряд
                    if all(x == 0 for x in row[j-k+1:j+1]):
                        return i
            else:
                count = 0
    return False

print("\nЗадание 2: Кинотеатр")
import ast
# пример: [[0,1,1,0], [1,0,0,0], [0,1,0,0]], 2
row_input = input("Введите список списков (пример [[0,1,1,0],[1,0,0,0],[0,1,0,0]]): ")
k = int(input("Сколько билетов требуется? "))
seats = ast.literal_eval(row_input)
print("Результат:", find_row(seats, k))


# --- Задание 3: Алгоритм RLE ---

def rle_encode(s):
    if not s:
        return ''
    result = []
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            result.append(f"{count}{prev}")
            prev = c
            count = 1
    result.append(f"{count}{prev}")
    return ''.join(result)

print("\nЗадание 3: Алгоритм RLE")
text = input("Введите строку для RLE: ")
print("Результат:", rle_encode(text))


# --- Задание 4: Шифр Цезаря ---

def caesar_cipher(text, key):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

print("\nЗадание 4: Шифр Цезаря")
message = input("Введите строку для шифрования: ")
shift = int(input("Введите ключ (0-25): "))
print("Результат:", caesar_cipher(message, shift))


# --- Задание 5: Табель успеваемости ---

print("\nЗадание 5: Табель успеваемости")
# Структура: {предмет: {фамилия: [оценки]}}
grades = {}

while True:
    line = input("Введите строку ('предмет фамилия оценка', пустая строка для выхода): ")
    if not line:
        break
    parts = line.split()
    if len(parts) != 3:
        print("Некорректный ввод. Введите 'предмет фамилия оценка'")
        continue
    subject, surname, mark = parts
    if subject not in grades:
        grades[subject] = {}
    if surname not in grades[subject]:
        grades[subject][surname] = []
    grades[subject][surname].append(mark)

for subject in grades:
    print(f"\n{subject}")
    for surname in grades[subject]:
        print(surname, ' '.join(grades[subject][surname]))
