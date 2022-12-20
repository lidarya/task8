# эта программа считает количество попыток, за которое компьютер угадывает одно случайное число
# ЕСЛИ НУЖНО ВЫВОДИТЬ СРЕДНЕЕ КОЛИЧЕСТВО ПОПЫТОК, ТО СМ. РЕШЕНИЕ ВО ВТОРОЙ ВЕРСИИ 

import numpy as np

def guess_number():
    
    # np.random.seed(100) # Если случайное число должно быть одинаковым
    random_number = np.random.randint(1, 101)
    # print(f'Random number = {random_number}')

    max = 101 # Upper limit of the range
    min = 1 # Lower limit of the range
    number = 0 # The final number = random_number
    count = 0 

    while True:
        count += 1
        middle = (max+min)//2
        if random_number == middle:
            number = middle
            break
        elif random_number>middle:
            min = middle
        else: max = middle
    
    # print(f'Number {number} guessed in {count} attempts')
    return count

print(f'Random number guessed in {guess_number()} attempts')