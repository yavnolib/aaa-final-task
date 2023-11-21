"""
    Напишите декоратор, который выводит имя
    функции и время выполнения — randint() ✅
    Бонус: декоратор принимает шаблон, в который
    подставляется время. ✅
"""
import random


def log(template="🛵 Delivered for {} s."):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) > 0 and len(kwargs) > 0:
                func(args, **kwargs)
            elif len(args) > 0 and len(kwargs) == 0:
                func(args)
            elif len(kwargs) > 0 and len(args) == 0:
                func(**kwargs)
            else:
                func()
            res = (
                f"{func.__name__} - {template.format(random.randint(1, 100))}"
            )
            print(res)
            return res

        return wrapper

    return decorator
