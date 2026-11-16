import random

print("Добро пожаловать в игру «Угадай число»!")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Введите вашу догадку: "))
    attempts += 1

    if guess < secret_number:
        print("Попробуйте больше.")
    elif guess > secret_number:
        print("Попробуйте меньше.")
    else:
        print("Поздравляем! Вы угадали число.")
        print("Количество попыток:", attempts)
        break



low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1
    print("Я думаю, это число", guess)
    answer = input("Твоё число больше, меньше или я угадал? ")

    if answer == "больше":
        low = guess + 1
    elif answer == "меньше":
        high = guess - 1
    elif answer == "угадал":
        print("Я угадал число!")
        print("Количество попыток:", attempts)
        break
    else:
        print("Пожалуйста, напиши: больше, меньше или угадал.")



#игра камень ножницы бумага
import random
user_score = 0
computer_score = 0
draws = 0
choices = ['камень','ножницы', 'бумага']
while True:
    user_choice = input(
        "Выберите: камень, ножницы или бумага: "
        "или выход для выхода из игры: "
    )
    if user_choice == 'выход':
        print("Выход из игры.")
        break
    elif user_choice not in choices:
        print("Неверный выбор. Попробуйте снова.")
        continue
    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        draws += 1
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'): 
        user_score += 1
        print("Вы выиграли!")
    else:
        computer_score += 1
        print("Вы проиграли!")
    print(f"Счёт: Вы {user_score} - {computer_score} Компьютер, Ничьи: {draws}")



number = int(input("Введите число: "))
count_number = 0
positive_count = 0
negative_count = 0
total_sum = 0
while number != 0:
    count_number += 1
    total_sum += number
    if number == 0:
        break
    elif number > 0:
        positive_count += 1
    else:
        negative_count += 1
    number = int(input("Введите число: "))

print(f"Количество введённых чисел: {count_number}")
print(f"Количество положительных чисел: {positive_count}")
print(f"Количество отрицательных чисел: {negative_count}")
print(f"Сумма всех чисел: {total_sum}")



number = int(input("Введите оценку: "))
five_count = 0
four_count = 0
three_count = 0
two_count = 0
one_count = 0
count = 0
average_sum = 0
while number != 0:
    if number < 1 or number > 5:
        print("Ошибка, оценка должна быть от 1 до 5. Попробуйте снова.")
    else:
        count += 1
        if number == 5:
            five_count += 1
        elif number == 4:
            four_count += 1
        elif number == 3:
            three_count += 1
        elif number == 2:
            two_count += 1
        elif number == 1:
            one_count += 1
        average_sum += number
    number = int(input("Введите оценку: "))
print(f"Количество пятерок: {five_count}")
print(f"Количество четверок: {four_count}")
print(f"Количество троек: {three_count}")
print(f"Количество двоек: {two_count}")
print(f"Количество единиц: {one_count}")
if count > 0:
    print(f"Средний балл: {average_sum / count}")
else:
    print("Оценки не были введены.")

    

number = int(input("Введите цену товара: "))
min_price = number
max_price = number
count = 0
average_sum = 0
total = 0
while number != 0:
    count += 1
    if number < min_price:
        min_price = number
    elif number > max_price:
        max_price = number
    average_sum += number
    total += number
    number = int(input("Введите цену товара: "))
print(f"Общее количество товаров: {count}")
print(f"Общая сумма цен: {total}")
print(f"Минимальная цена: {min_price}")
print(f"Максимальная цена: {max_price}")
print(f"Средняя цена; {average_sum / count}")

