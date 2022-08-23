import traceback


def factorial(end_range: int):

    try:
        fact = 1

        if end_range >= 0:
            for i in range(1, end_range + 1):
                fact *= i

            return fact
        else:
            raise ValueError(f"Must use positive integer for factorial(fact): {fact} and end of range: {end_range}")
    except Exception as e:
        raise ValueError(f"{e} {traceback.format_exc()}")




