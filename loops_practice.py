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