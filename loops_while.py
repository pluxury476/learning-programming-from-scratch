# задача 1 выведи числа от 1 до 10 через while
i = 1 
while i <= 10:
    print(i)
    i += 1

print("---")

# задача 2 посчитай сумму всех  четных чисел от 1 до 40
i = 1
total = 0
while i <= 40:
    if i % 2 == 0:
        total += i
    i += 1
print(total)

print("---")

# задача 3 начни с числа 100 и уменьшай его на 5 в цикле while
i = 100
while i > 0:
    i -= 5
    print(i)

print("---")

# задача 4 программа задала числo , ты вводишь числа с клавиатуры,пока не угадаешь
secret = 90
attempts = 0
guess = int(input("Угадай число от 1 до 105:"))
while guess != secret:
    attempts += 1
    if guess < secret:
        guess = int(input("мало,пробуй еще уебище:"))
    elif guess > secret:
        guess = int(input("много,пробуй еще уебище:"))
attempts += 1 
print(f"ай лев красавчик ты угадал, но ты ебень потратил на это {attempts} попыток")


print("---")

# задача 5 пользователь вводит числа, они складываются. Когда введет 0, программа выводит сумму всех введенных чисел
total = 0
while True:
    number = int(input("Введите число (0 для выхода): "))
    if number == 0:
        break
    total += number
print(f"Сумма всех введенных чисел: {total}")

print('---')

#задача 6 сумма до повышения на 50
total = 0
while True:
    number = int(input())
    total += number
    if total > 50:
        break
print(f"Сумма превысила 50! Итог: {total}")


