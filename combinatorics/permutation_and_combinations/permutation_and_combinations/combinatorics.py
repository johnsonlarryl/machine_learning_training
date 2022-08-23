import traceback


def factorial(n: int):
    """
    :param n: Input of integer
    :return: Factorial of integer
    """
    try:
        if n >= 0:
            if (n == 0) or (n == 1):
                return 1
            else:
                return n * factorial(n - 1)

            return fact
        else:
            raise ValueError(f"Must use positive integer for {n}")
    except Exception as e:
        raise ValueError(f"{e} {traceback.format_exc()}")


def permutation(n: int, r: int):
    """
    :param n: Number of elements in collection or list
    :param r: Number of elements in each pair
    :return: Permutation of collection and pairs
    """
    return factorial(n) / factorial(n-r)


def combination(n: int, r: int):
    """
    :param n:Number of elements in collection or list
    :param r: Number of elements in each pair
    :return: Combination of collection and pairs
    """
    return factorial(n) / (factorial(n-r) * factorial(r))

