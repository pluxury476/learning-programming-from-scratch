# задача 2 посчитай сумму всех чисел от 1 до 50
total = 0
for i in range(1,51):
    total += i
    print(total)

print("---")

# задача 3 выведи все нечетные числа от 1 до 30
for i in range(1,31):
    if i % 2 != 0:
        print(i)

print("---")

#задача 4 выведи числа от 20 до 0 с шагом 3
for i in range(20,0,-3):
    print(i) 

    print("---")

#задача 5 дано слово "программирование",посчитай,сколько в нем гласных букв
word = "программирование"
count = 0
for letter in word:
    if letter in "аеёиоуыэюя":
        count += 1
        print(count)

print("---")

#задача 6 спроси высоту потом нарисуй елку
n = int(input("Высота елки: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("---")

#задача 7 сделай тоже самое но чтобы было 2 треугольника
n = int(input("Высота елки: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

print("---")

# задача 8 гласные и согласные буквы

word = input("Введите слово:")
vowels = 0
consonants = 0
for letter in word:
    if letter in "аеёиоуыэюя":
        vowels += 1
    else:
        consonants += 1
        print(f"Гласные: {vowels}, Согласные: {consonants}")

print("--- ")

#задача 9 выведи сила от 1 до 30 если делится на 3 - fizz, на 5 - buzz, на 15 - fizzbuzz,иначе - само число
for i in range(1,31):
    if i % 15 == 0:
        print( "fizzbuzz") 
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

print("---")

#задача 10 спроси слово,спроси гласные,но обязательно через continue
word = input("Введите слово: ")
count = 0
for letter in word:
    if letter not in "аеёиоуыэюя":
        continue 
    count += 1 
print(f"гласные: {count}")

print("---")

#задача 11 таблица умножения на 7 пропусти строки где результат делится на 5 и остановись если больше 50

for i in range(1, 11):
    total = 7 * i
    if total > 50:
        break
    elif total % 5 == 0:
        continue
    print(f"7 * {i} = {total}")
    