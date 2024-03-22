# cтворюємо зовнішню ф-цію caching_fibonacci за параметром cache
# який є пустим словником
def caching_fibonacci(cache = {}):
    
    # створюємо функцию fibonacci, яка обчислює число Фібоначчі
    # за допомогою рекурсії
    def fibonacci(n):
       
        # базовий випадок рекурсії,
        # у якій n менший, або дорівнює, 0 у словнику повертає 0:
        if n <= 0:
            return 0
        
        # базовий випадок рекурсії,
        # у якій n якщо є 1 у словнику повертає 1
        elif n == 1:
            return 1
        
        # якщо n вже є у словнику, повертає теж саме значення,
        # використовуючи інформацію, яка вже є у кеші, тобто словнику
        elif n in cache:
            return cache[n]

        # рекурсивний випадок, у якому обчислюється 
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(2))  
print(fib(3))

#     ФУНКЦІЯ fibonacci(n)
#         Якщо n <= 0, повернути 0
#         Якщо n == 1, повернути 1
#         Якщо n у cache, повернути cache[n]

#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         Повернути cache[n]

#     Повернути функцію fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci
