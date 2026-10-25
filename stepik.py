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
