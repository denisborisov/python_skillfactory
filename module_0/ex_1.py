'''
Задание.

Компьютер загадывает целое число от 1 до 100, и нам нужно написать программу, которая угадывает число
за как можно меньшее количество попыток.
'''

import np

def guesswork(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''

    trials = 1
    prediction = np.random.randint(1, 101)
    while prediction != number:
        trials += 1

        if prediction < number:
            prediction -= (prediction - number) // 2

        elif prediction > number:
            prediction += (number - prediction) // 2

    return trials


def score_game(guesswork):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    trials_list = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        trials_list.append(guesswork(number))

    score = int(np.mean(trials_list))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


score_game(guesswork)