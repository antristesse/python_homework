# Task 1

import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        logger.info("")

        return result

    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

say_hello()

@logger_decorator
def check_grades(*grades):
    return True

check_grades(85, 90, 78)

@logger_decorator
def record_student(**student_info):
    return logger_decorator

record_student(name="Ana", course="Python", grade=95)

