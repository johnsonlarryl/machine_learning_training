import traceback


def factorial(fact: int, end_range: int):
    try:
        if (fact >= 0) and (end_range >= 0):
            for i in range(1, end_range + 1):
                fact *= i

            return fact
        else:
            raise ValueError(f"Must use positive integer for factorial(fact): {fact} and end of range: {end_range}")
    except Exception as e:
        raise ValueError(f"{e} {traceback.format_exc()}")




