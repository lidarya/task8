import numpy as np

def average_attempts():
    count_ls = [] # Cписок для сохранения попыток
    
    # np.random.seed(100) # Если нам нужно random_array = const
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел

    for random_number in random_array:
        max = 101 # Верхняя граница диапазона, в него не включается
        min = 1 # Вижняя граница диапазона, в него включается
        count = 0 # Счётчик попыток угадывания
    
        while True:
            count += 1
            middle = (max+min)//2 # Среднее число диапазона
            if random_number == middle:
                break
            elif random_number>middle:
                min = middle # Отбрасываем нижнюю половину диапазона
            else: max = middle # Отбрасываем верхнюю половину диапазона

        count_ls.append(count)

    average = int(np.mean(count_ls)) 
    return average
    
print(f'On average, your algorithm guesses the number in {average_attempts()} attempts')

