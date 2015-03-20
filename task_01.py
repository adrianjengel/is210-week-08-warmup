#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK8 warmup task_01 - Fibonacci sequence generator function."""


def fibonacci(maxint):
    """Building a Fibonacci sequence generator function.

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

    newlist = []
    val1, val2 = 1, 0
    while val2 < maxint:
        newlist.append(val2)
        val1, val2 = val2, val1+val2
    return newlist
