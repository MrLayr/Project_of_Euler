Fibanacci = [1, 2] #Посчитать сумму четных чисел фибаначи до 4 млн
Fibanacci_copy = []
FibaSum = 0
j = 0
for i in range(4000000-1):
    if j < 900:
        Fibanacci.append(Fibanacci[j] + Fibanacci[j+1])
        j += 1
    else:
        Fibanacci_copy.append(Fibanacci[j-1])
        Fibanacci_copy.append(Fibanacci[j])
        Fibanacci = Fibanacci_copy
        j = 0
    if Fibanacci[j] % 2 == 0:
        FibaSum += Fibanacci[j]

print(FibaSum)
