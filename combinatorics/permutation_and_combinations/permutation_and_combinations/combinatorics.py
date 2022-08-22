def factorial(fact: int, end_range: int):
    for i in range(1, end_range + 1):
        fact *= i

    return fact
