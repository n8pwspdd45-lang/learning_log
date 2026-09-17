a = int(input("a: "))
b = int(input("b: "))

somma = 0

for i in range(a, b+1):
    i = int(i)
    if i % 2 == 1:
        somma += i
    else:
        pass

print(f"somma = {somma}")