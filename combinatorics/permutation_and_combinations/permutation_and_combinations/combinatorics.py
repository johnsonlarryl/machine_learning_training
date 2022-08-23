import traceback


def factorial(n: int):

    try:
        fact = 1

        if n >= 0:
            if (n == 0) or (n == 1):
                return 1
            else:
                return n * factorial(n - 1)

            return fact
        else:
            raise ValueError(f"Must use positive integer for factorial(fact): {fact} and end of range: {end_range}")
    except Exception as e:
        raise ValueError(f"{e} {traceback.format_exc()}")




