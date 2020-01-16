'код не аптимизирован, выполнение занимает примерно 3-5 минут, можно иправить сохраняя промежуточные результаты например в файл ответ 10001 простое число 104743'
'test_num_array = [i for i in range(2, 10)]'
num_flag = 0
'entered_num = int(input())'
for num in range(2, 500000):
    tmp_flag = 'Простое'
    for j in range(2, num):
        if num % j == 0:
            tmp_flag = 'Не простое'
            break
    if tmp_flag == 'Простое':
        num_flag += 1
        if num_flag == 10001:
            print(num)
            break




