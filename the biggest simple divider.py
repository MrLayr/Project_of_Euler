#num = 600851475143  Найти наибольший простой делитель этого числа
#если искомое число больше указанного выше нужно raige в обеих функциях уеличить
def Prostoe (num):
    count = 0
    numbers = [i for i in range (10000)]
    for number in numbers[1:]:
        if num % number == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def Bolsh_del (n):
    Biger = 0
    numbers = [i for i in range(10000)]
    for num in numbers[1:]:

        if n % num == 0 and Prostoe(num) and num > Biger:
            Biger = num
    return Biger

print (Bolsh_del(600851475143))
