import re
from typing import Callable


def generator_numbers(text: str):
    numbers = re.findall(r"\d+\.\d+", text)
    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable):
   total_sum = 0
   numbers_generator = func(text)
   for number in numbers_generator:
       total_sum = total_sum + number
   return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."      
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") 