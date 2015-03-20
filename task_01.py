#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK8 warmup task_01 - Fibonacci sequence generator function."""


def fibonacci(maxint):
    """Building a Fibonacci sequence generator function with the while loop.

    Args:
        int: This will serve as the upper bound of the loop.
    Returns:
        list: Returns the newly generated sequence as a list.

    Example:
    >>> fibonacci(50)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> fibonacci(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    """
    val1, val2 = 0, 1
    newlist = [val1, ]
    while val2 < maxint:
        val1, val2 = val1, val1+val2
        newlist.append(val1)
    return newlist
