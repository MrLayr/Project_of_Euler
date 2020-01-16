numbers = [i for i in range(1001)] # Все числа до 1000 кратные 3 или 5
right_numbers = []
for j in numbers:
    if j != 0 and (j % 3 == 0 or j % 5 == 0):
        right_numbers.append(j)
print(right_numbers)
print(len(right_numbers))
