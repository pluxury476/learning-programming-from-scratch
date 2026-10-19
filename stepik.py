## степик задачи(скипнул до 7.4,плюс дипсик задачи немного 

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
