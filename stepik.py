# степик задачи(скипнул до 7.4,плюс дипсик задачи немного 

# задача 1 Выведи числа от 1 до 10, но остановись, когда дойдёшь до 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("---")

#задача 2 пропусти тройку
for i in range(1,8):
    if i == 3:
        continue
    print(i)

print("---")

#задача 3 только четные числа от 1 до 20
for i in range(1,21):
    if i % 2 != 0:
        continue
    print(i)

print("---")

#задача 4 остановись на слове "стоп"
while True:
    word = input("Введи слово:")
    if word == "стоп":
        break
print("Пока!")
    

print("---")

#задача 5 начинаем строковые значения 

word = "привет"
print("Слово: ", word)
print(word[::-1])

#задача 6 выведи слово заглавными буквами и посчитай длину
word = "привет"
print("Слово: ", word)
print(word.upper())
print("Длина:",len(word))

#задача 7 выведи имя с большой буквы
word = input("Имя: ")
print(f"Привет, {word.capitalize()}")

#задача 8 сколько раз встречается буква
word = input("Слово: ")
letter = input("Буква: ")
print(f"Буква '{letter}' встречается {word.count(letter)} раза")

print("---")

#задача 9 первая и последняя
word = input("Слово: ")
print(f"Первая: {word[0]}")
print(f"Последняя: {word[-1]}")

print("---")

#задача 10 каждая 2 буква
word = input("Слово: ")
print(f"{word[::2]}")

print("---")

#задача 11 задом наперед + заглавные
word = input("Слово: ")
print(f"{word.upper()[::-1]}")

print("---")

#задача 12 заменить букву
word = input("Слово: ")
print(f"{word.replace("о", "а")}")

#задача 13 слова в предложении
word = input("Предложение: ")
words = word.split()
print(f"Слов: {len(words)}")

#задача 14 убрать все пробелы
word = input("Предложение: ")
print(f"{word.replace(" ","")}")

#задача 15 заглавные первые буквы слов 
word = input("Предложение: ")
print(f"{word.title()}")

#задача 16 перемешанный палидром
word = input("Слово: ")
if word.lower() == word.lower()[::-1]:
    print("Это палиндром")
else:
    print("Не палиндрон")

#задача 17 шифр цезаря легкий 
alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
word = "Привет"
result = ""
for i in word:
    if i in alp:
        pos = alp.index(i)
        post = (pos + 1) % len(alp)
        result += alp[post]
    else:
        result += i
print(result)


###СПИСКИ 
#задача 1
list = ['хлеб', 'молоко', 'яйца',]
list.append("Сыр")
print(f"Длина: {len(list)}")

#задача 2 max min
list = [5, 8, 10, 40,2]
max_wal = list[0]
min_wal = list[0]
for n in list:
    if n > max_wal:
        maxwal = n
    if n < min_wal:
        minwal = n
print(f"Максимум {max_wal}")
print(f"Минимум {min_wal}")

#задача 3 привыкаю к спискам
colors = ["красный", "зелёный", "синий"]
print(colors[0])
print(colors[-1])

colors.append("желтый")
print(colors)

colors[1] = "оранжевый"
print(colors)

colors.remove("синий")
print(colors)

for c in colors:
    print("Цвет:", c)

print("Всего цветов:", len(colors))

#задача 4 фильтр оценок
grades = [3, 5, 2, 4, 5, 3, 4, 2, 5]
good_grades = []
for n in grades:
    if n >= 4:
        good_grades.append(n)
print(good_grades)

#задание 5 только черные 
grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chetko = []
for n in grades:
    if n % 2 == 0:
        chetko.append(n)
print(chetko)

#задача 6 сумма хороших оценок 
grades = [3, 5, 2, 4, 5, 3, 4, 2, 5]
chetko = []
for n in grades:
    if n >= 4:
        chetko.append(n)
print(f"Сумма: {sum(chetko)}")

#задача 7 слова длиннее 4 букв
words = ["кот", "собака", "дом", "дерево", "ёж", "компьютер"]
long_word = []
for n in words:
    if len(n) > 4:
        long_word.append(n)
print(long_word)

#задача 8 любимые игры
games = []
for n in range(3):
    game = input(f"Игра {n + 1}:")
    games.append(game)
print(f"Мои игры: {games}")
print(f"Всего: {len(games)}")

#задача 9 фильтрация
numbers = [5, -3, 10, -7, 2, 0, -1]
positive = []
for n in numbers:
    if n > 0:
        positive.append(n)
print(positive)

#задача 10 подсчет слов
word = input("Предложение: ")
words = word.split()
print(f"Слов: {len(words)}")

 #задача 11 фильтр имен
names = ["Антон", "Ян", "Екатерина", "Лев", "Александр"]
short_names = []
for n in names:
    if len(n) <= 4:
        short_names.append(n)
print(short_names)

#задача 12 заглавные строки
words = ["привет", "как", "дела"]
capitalized = []
for n in words:
    capitalized.append(n.capitalize())
print(capitalized)

#задача 13 выведи длину и выведи наоборот
word = input("Слово: ")
print(f"Длина: {len(word)}")
print(f"Наоборот: {word[::-1]}")
if word == word[::-1]:
    print("Это палиндром")
else:
    print("Обычное слово")

#задача 14 спортсмены 
athletes = ["Иван", "Олег", "Анна", "Дмитрий", "Ян"]
short_names = []
for n in athletes:
    if len(n) <= 4:
        short_names.append(n)
print(short_names)

#задача 15 секретное слово
word = input("Слово: ")
print(f"Наоборот: {word[::-1]}")
print(f"Заглавные: {word.upper()}")
print(f"Длина: {len(word)}")

## функции
#задача 1 функция приветствие
def say_hello():
    print("Привет, я внутри функции!")
    print("Меня вызвали, и я работаю,")

say_hello()
say_hello()
say_hello()

#задача 2 функция приветствие с именем
def introduce(name, age):
    print(f"Меня зовут {name}, мне {age} лет.")
introduce("Иван",18)

#задача 3 учимся return
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result_add = add(5, 3)
print(f"Сумма: {result_add}")

result_mult = multiply(4, 6)
print(f"Произведение: {result_mult}")

result = multiply(add(2,3), 10) #функция внутри функции
print(f"Результат композиции: {result}")

#задача 4 функции для среднего балла
def get_average(grades):
    return sum(grades) / len(grades)

# проверка функции
grades = [4, 5, 3, 4, 5, 5, 4]
average = get_average(grades)
print(f"Средний балл: {average}")

#задача 5 фильтрация хороших оценок 
def good_grades(grades):
    good = []
    for n in grades:
        if n >= 4:
            good.append(n)
    return good

grades = [3, 5, 2, 4, 5, 3, 4, 2, 5]
filtred_grades = good_grades(grades)
print(f"Хорошие оценки: {filtred_grades}")

for i in range(1, 11):
    print(i)

numbers = [3, 7, 2, 9, 4]
total = 0
for n in numbers:
    total += n
print(total)

numbers = [1, 4, 7, 10, 13, 16, 20]
total = 0
for n in numbers:
    if n % 2 == 0:
        total += n
print(total)

num = int(input())
prev = num % 10
num = num // 10
is_sorted = True
while num > 0:
    current = num % 10
    if current < prev:
        is_sorted = False
        break
    prev = current
    num = num // 10
if is_sorted:
    print("YES")
else:
    print("NO")

n = int(input())
count = 0
while n > 0:
    last = n % 10
    if last % 2 == 0:
        count += 1
        print(f"{count}-я четная цифра равна {last}")
    n = n // 10
print(f"Всего четных цифр: {count}")

# найти наименьший делитель числа   

# вложенные циклы 
total = 0
for n in range(1,14):
    for k in range(1,13):
        for m in range(1,12 ):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print("n =", n, "k =", k, "m =", m)
print("Общее кольчество натуральных решений =", total)

total = 0
for x in range(1,11):
    for y in range(1,21):
        for z in range(1,201):
            if 10 * x + 5 * y + 0.5 * z == 100 and x + y + z == 100:
                total += 1
                print("x =", x, "y =", y, "z =", z)
print("Общее количество =", total)

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = sum ** (1/5)
                e = round(e)
                if e ** 5 == sum and e <= 150:
                    print(a + b + c + d + e)
                    break

## внутренние циклы 2
n = int(input())
for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0: 
            print("+", end='')
    print()


# Дано натуральное число число n,напишите программу которая печатает численний треугольник с высатой равной n
n = int(input())
total = 1
for i in range(1, n + 1):
    for j in range(1,i +1):
        print(total, end=' ')
        total += 1
    print()

# На вход программе подается два натуральных числа a и b (a<b). Напишите программу, которая находит все простый сила от a до b включительно.
a = int(input())
b = int(input())
for n in range(a, b + 1):
    prime = True
    for j in range(2, n):
        if n % j == 0:
            prime = False
            break
    if prime and n > 1:
        print(n)

#сумма факториалов
a = int(input())
total = 0
factorial = 1
for i in range(1, a + 1):
    factorial *= i
    total += factorial
print(total)    


n = int(input())
m = int(input())
found = False
for banana in range(1, n):
    for diamond in range(1, n):
        for deer in range(1, n):
            if banana + 3 * diamond + 2 * deer == m:
                print(f"{banana} + 3x{diamond} + 2x{deer} = {m}")
                found = True

if not found:
    print("Нет решения")

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')

    for k in range(i - 1,0, -1):
        print(k, end='')
    print()

# Как вы могли заметить, Тимур очень любит математику. Это проявляется во всём – даже когда он видит время на часах. Особенно Тимуру нравятся такие моменты времени, когда число часов h , возведенное в некоторую натуральную степень n, равняется количеству минут m
n = int(input())
for h in range(24):
    m = h ** n
    if m < 60:
        print(f"{h:02d}:{m:02d}")

#дано число n > 99,найдите её третью цифру сначала
n = int(input())
while n >= 1000:
    n //= 10
third_digit = n % 10
print(third_digit)

n = int(input())
last_digit = n % 10
count_3 = 0
count_last = 0
count_even = 0
sun_5 = 0
prod_7 = 1
count_0_5 = 0
while n > 0:
    digit = n % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sun_5 += digit
    if digit > 7:
        prod_7 *= digit
    if digit == 0 or digit == 5:
        count_0_5 += 1
    n //= 10

print(count_3)
print(count_last)
print(count_even)
print(sun_5)
print(prod_7)
print(count_0_5)

# ## задачи степик 9.1
#1
s = "In 2010, someone paid 10k bitcoin for two pizzas."
print(s[7])

#2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[39])

#3
n = "abcdefg"
for c in range(0, len(n), 2):
    print(n[c])

# 4
n = "abcdefg"
for c in range(1, len(n) + 1):
    print(n[-c])

# 5 
f = 'Петров'
i = 'Иван'
o = 'Сидорович'
initials = f[0] + i[0] + o[0]
print(initials)

# 6
n = input()
s = 0
for i in range(len(n)):
    s += int(n[i])
print(s)

#7
n = input()
s = "Цифр нет"
for i in range(len(str(n))):
    if n[i] in "0123456789":
        s = "Цифра"
        break
print(s)

#8
n = input()
star = 0
plus = 0
for i in range(len(n)):
    if i == "*":
        star += 1
    elif i == "+":
        plus += 1
print(f"Символ * встречается {star} раз")
print(f"Символ + встречается {plus} раз")

#9
a = input()
count = 0
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
print(count)

#10
s = input()
gl = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
sog = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
son, cons = 0, 0
for c in s:
    if c in gl:
        son += 1
    if c in sog:
        cons += 1
print('Количество гласных букв равно', son)
print('Количество согласных букв равно', cons)

# 11
n = int(input())
d = ''
while n > 0:
    d = str(n % 2) + d
    n = n // 2
print(d)

print("---")

s = input()
for i in range(len(s)):
    if i >= len(s) // 2 :
         print(s[i], end='')

#строки
word = input()
print(len(word))
print(word * 3)
print(word[0])
print(word[0: 3])
print(word[-3:])
print(word[::-1])
print(word[1:])
print(word[1:-1])

#
word = input()
print(word[2])
print(word[-2])
print(word[:5])
print(word[0:-2])
print(word[0::2])
print(word[1::2])
print(word[::-1])
print(word[::-2])

#На вход программе подаётся строка текста. Напишите программу, которая разрежет её на две равные части, переставит их местами и выведет на экран.
word = input()
length = len(word)
half_length = length // 2
first_half = word[:half_length]
second_half = word[half_length:]    
print(second_half + first_half)

text = input()
first = text.find("a")
last = text.rfind("a")
result = text[first + 1:last]
print(result)

# повтор

n = int(input())
count = 0
for i in range(5):
    if n % 2 == 0:
        count += 1
    n = n // 10
print(count)

n = int(input())
for i in range(n, 0, -1):
    print(i)
print("Старт!")

word = input()
n = input()
if n in word:
    print("Да")
else:
    print('Нет')

word = input()
print(word[::-1])
print(word.upper())

word = input()
count = 0
for char in word:
    if char in "аеёиоуыэюя":
        count += 1
print(count)

n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=' ')
    print()

max_weight = 0
weight = ''
for i in range(3):
    w =  input()
    current_weight = 0

    for char in w:
        current_weight += ord(char)
    if current_weight > max_weight:
        max_weight = current_weight
        weight = w
print(weight)
first = input()
max_word = first
min_word = first

for i in range(3):
    word = input()
    if word > max_word:
        max_word = word
    if word < min_word:
        min_word = word
last_min = min_word[-1]
last_max = max_word[-1]

code_min = ord(last_min)
code_max = ord(last_max)

magic = (code_min * code_max) ** 2
print(magic)

total = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        total += num
print(total)

word = input()
print(f"Ввод: {word}")
print(f"Вывод: {word[1]} {word[-1]}")

word = input()
polid = word[::-1]
if word == polid:
    print("YES")
else:
    print("NO")

num = int(input())
for i in range(num):
    for j in range(num):
        print("*", end='')
    print()






