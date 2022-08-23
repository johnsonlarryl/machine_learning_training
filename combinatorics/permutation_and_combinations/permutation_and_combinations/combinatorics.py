import traceback
from typing import Any, List, Tuple

PERMUTATION = "perm"
COMBINATION = "comb"


def factorial(n: int) -> int:
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


def permutation(n: int, r: int) -> int:
    """
    :param n: Number of elements in collection or list
    :param r: Number of elements in each pair
    :return: Permutation of collection and pairs
    """
    return int(factorial(n) / factorial(n-r))


def combination(n: int, r: int) -> int:
    """
    :param n:Number of elements in collection or list
    :param r: Number of elements in each tuple
    :return: Combination of collection and pairs
    """
    return int(factorial(n) / (factorial(n-r) * factorial(r)))


def combinatorics_list(s: List[Any], r: int, algo=PERMUTATION) -> List[Tuple]:
    """
    :param s: List or collection of elements
    :param r:  Number of elements in each tuple
    :param algo: Enumerated combinatorics algorithm of choice 'combo' for Combinations and "perm" for Permutations
    :return: List of Combinations or Permutations
    """
    temp_tuple = []

    if algo == PERMUTATION:
        running_list = []
    elif algo == COMBINATION:
        running_list = set()
    else:
        raise NotImplemented(f"algo of type {algo} is not supported.")

    for i in range(len(s)):
        if temp_tuple:  # There could still be data to process
            add_item(running_list, temp_tuple, algo)

        temp_tuple = [s[i]]

        for j in range(len(s)):
            if i == j:
                continue  # We do not want a tuple of the same index, so skip.

            if len(temp_tuple) < r:
                temp_tuple.append(s[j])
            else:
                add_item(running_list, temp_tuple, algo)
                temp_tuple = [s[i], s[j]]

    if temp_tuple:  # There could still be data to process
        add_item(running_list, temp_tuple, algo)

    return running_list


def add_item(collection: Any, temp_tuple: List, algo=PERMUTATION) -> None:
    """
    :param collection:  List or collection of elements
    :param temp_tuple: Temporary data structure to hold elements in flight for processing
    :param algo: Enumerated combinatorics algorithm of choice 'combo' for Combinations and "perm" for Permutations
    """
    error_message = f"collection is of type {type(collection)} is not supported."

    if algo == PERMUTATION:
        if isinstance(collection, list):
            collection.append(tuple(temp_tuple))
        else:
            raise NotImplemented(error_message)
    elif algo == COMBINATION:
        if isinstance(collection, set):
            if is_unique(collection, tuple(temp_tuple)):
                collection.add(tuple(temp_tuple))  # Only add if the tuple is unique, including the reverse tuple
        else:
            raise NotImplemented(error_message)
    else:
        raise NotImplemented(error_message)


def is_unique(collection: set, a: Tuple) -> bool:
    b = a[::-1]

    return b not in collection

