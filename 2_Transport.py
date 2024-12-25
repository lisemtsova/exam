
rows = int(input("Сколько всего поставщиков?: "))
cols = int(input("А сколько потребителей?: "))

matrix = []

print(f"Заполните матрицу тарифов, где A-поставщики, B-потребители:")

for i in range(cols):
    print(f" B{i+1}", end = " ")
print()
for i in range(rows):
    row = list(map(int, input(f"А{i+1} ").split()))
    matrix.append(row)

supl = list(map(int, input("Введите запасы всех поставщиков через пробел:").split()))
needs = list(map(int, input("Введите потребности всех потребителей через пробел:").split()))

if sum(supl) == sum(needs):
    print("Задача сбалансирована")
else:
    print("Задача не сбалансирована. Нужно добавить фиктивного поставщика или потребителя")

