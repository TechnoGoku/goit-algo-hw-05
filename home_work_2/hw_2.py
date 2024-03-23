import re
from typing import Callable


def generator_numbers(text: str):
    numbers_text = []
    numbers = re.findall(r"\d+\.\d+", text)


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# def sum_profit(text: str, func: Callable):
#     pass
        
 