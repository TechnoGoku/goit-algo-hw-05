import re
from typing import Callable


def generator_numbers(text: str):
    numbers_text = []
    numbers = re.findall(r"\d+\.\d+", text)
    for number in numbers:
        numbers_text.append(number)
        print(numbers_text)
        yield float(number)



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
num_gen = generator_numbers(text)
for number in num_gen:
    print(number)

# def sum_profit(text: str, func: Callable):
#     pass
        
 