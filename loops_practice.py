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
