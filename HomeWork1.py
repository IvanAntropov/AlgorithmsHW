# Необходимо сравнить скорость работы 2 алгоритмов вычисления чисел Фибоначчи и определить, 
# какой из них работает быстрее. Так различия начнутся уже с 40 члена последовательности.

from datetime import datetime
import time
import timeit
from cmath import sqrt


def firstDef(number: int) -> int:
    if number == 2:
        return 1
    elif number == 1:
        return 1
    else:
        return firstDef(number-1) + firstDef(number-2)
    
    
def secondDef(number: int) -> int:
    firstN = 1
    secondN = 1
    sumN = 0
    for i in range(number - 2):
        sumN = firstN + secondN
        firstN = secondN
        secondN = sumN
    return sumN     


def thirdDef(number: int) -> int:
    sqrtFive = sqrt(5)
    firstPart = ((1 + sqrtFive)/2)**number
    secondPart = ((1 - sqrtFive)/2)**number
    return round(((firstPart - secondPart)/sqrtFive).real)
    
    
start_time1 = time.time()
print(firstDef(40))
time.sleep(1) 
print(f"Время выполнения первого алгоритма: {(time.time() - start_time1) - 1}\n") # O(2^n)

start_time2 = time.time()
print(secondDef(3000))
time.sleep(1) # время не замеряет 0.0 пишет, а там delta и т.п.(
print(f"Время выполнения второго алгоритма: {(time.time() - start_time2) - 1}\n") # O(N)

start_time3 = time.time()
print(thirdDef(1000))
time.sleep(1)  # время не замеряет 0.0 пишет, а там delta и т.п.(
print(f"Время выполнения третьего алгоритма: {(time.time() - start_time3) - 1}\n")  # близко к O(LogN)?


#---------------------------------------------------------------------------------------------------------------------------------
#
# Выходит так, что самый быстрый алгоритм получился третий, но при числе 1500 выдает StuckOverFlow и в этом он проигрывает второму,
# разница по времени у них небольшая, так что второй тут лучший, первый же в свою очередь на числе 40 уже работает 12 сек, 
# а 50 я устал ждать)
# 
# Не знаю где применить рекурсию, кроме как собеседования долго и муторно 
#
#---------------------------------------------------------------------------------------------------------------------------------





