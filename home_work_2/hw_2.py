# імпортуємо модулі для роботи з регулярними виразами та аннотацій типів данних 
import re
from typing import Callable

# створюємо функцію с текстовим параметром, яка читає усі дійсні числа та повертає генератор
def generator_numbers(text: str):
    numbers = re.findall(r"\d+\.\d+", text)
    for number in numbers:
        yield float(number)

# створюємо функцію, яка приймає прочитані дійсні числа та функцію, генератор, який ми створили, яка ітерується по дійсним числам та сумує їх, та повертає результат суми цих чисел
def sum_profit(text: str, func: Callable):
   total_sum = 0
   numbers_generator = func(text)
   for number in numbers_generator:
       total_sum = total_sum + number
   return total_sum

# визначаємо текст, з яким буде прцювати генератором
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."      
# створюємо генератор для обчислення загальної суми усієї заробітної плати 
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") 