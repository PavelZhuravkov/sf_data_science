""" Игра угадай число.
Компьютер сам загадывает иугадывает число.
"""
import numpy as np

def random_predict(number:int=1)->int:
	""" Рандомно угадываем число

  Args:
    number(int,optional): Загаданное число.Defaults to 1.

  Returns:
    int: Число попыток.
    """
	count=0
	a=1
	b=101
	while True:
		count+=1
		predict_number=int((a+b)/2) # Используем метод деления пополам, сужаем границы поиска.
		if predict_number>number:   # Если предполагаемое число больше заданного,
			b=predict_number           # уменьшаем в 2 раза правую границу(b).
		elif predict_number<number: # Если предполагаемое число меньше заданного,
			a=predict_number           # уменьшаем в 2 раза левую границу(b).
		else:                       # Если ни одно из вышеперечисленных условий   
			break                      # не выполняется, значит BINGO!!!!!!
	return (count)
print(f"Количество попыток {random_predict()}")



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__=='__main__':
    score_game(random_predict)
    