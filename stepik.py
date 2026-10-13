### степик задачи(скипнул до 7.4,плюс дипсик задачи немного 

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
