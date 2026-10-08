print("уже дошел до урока 7。4 на степике“）

# 08.30 я выполнил пароу задач и вышли вот такие коды 
total = 0
n = int(input())
for i in range(1, n + 1):
    if i % 2 != 0:
        total += i
    else:
        total -= i
print(total)  

# щас будет еще один

total = 0
for i in range(1, 10 + 1):
    num = int(input())
    if num % 2 == 0:
        total += 1
if total == 10:
    print("YES")
else:
    print("NO")

