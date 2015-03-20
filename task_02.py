#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK8 warmup task_02 - if statement practice."""


def bool_to_str(bval):
    """Practice the use of the if statement.

    Args:
        bool: A boolean-like value that can be evaluated for truthiness or
        falsiness.
    Returns:
        str: Returns either 'Yes' or 'No', depending on evaluation.

    Example:
    >>> bool_to_str(5)
    'Yes'
    >>> bool_to_str('')
    'No'

    """
    if bval:
        retval = 'Yes'
    else:
        retval = 'No'
    return retval
