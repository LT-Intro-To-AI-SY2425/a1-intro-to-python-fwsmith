"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if n < 0:
        return -1 * n
    else:
        return n


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    if n > 0:
        input = n
        output = input
        input = input - 1
        while input > 0:
            if input > 0:
                output = output * input
                input = input - 1
            else: 
                return output
        return output
    else: 
        if n == 0:
            return 0
        else:
            return "DNE"


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    output = []
    for value in lst:
        if lst.index(value) % 2 == 0:
            output.append(value)
    return output

def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    sum = 0
    for value in lst:
        sum += value
    return sum


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    sum = 0
    for value in lst:
        sum += value
    return sum / len(lst)


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[(len(lst) // 2) - 1]) // 2
    else: 
        return lst[len(lst) // 2]


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    gooselst = []
    remainder = 0
    while len(lst) > 2:
        for name in lst: 
            if (lst.index(name) + (1 + remainder)) % 3 == 0:
                gooselst.append(name)
        remainder = len(lst) % 3
        for name in lst:
            for x in gooselst:
                if name == x:
                    lst.remove(name)
    return lst

    raise NotImplementedError("duck_duck_goose")


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert factorial(-4) == "DNE", "factorial of -4 failed"
    assert factorial(0) == 0, "factorial of 0 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert every_other(["alpha", "beta", "delta", "gamma", "sigma"]) == [
        "alpha",
        "delta",
        "sigma",
    ], "every_other of [alpha, beta, delta, gamma, sigma] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5, 6]) == 3, "median of [1,2,3,4,5,6] failed"
    assert median([5, 2, 1, 3, 4]) == 3, "median of [5,2,1,3,4] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")