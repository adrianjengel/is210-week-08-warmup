#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK8 warmup task_03 - for loop practice."""

import decimal


def lexicographics(to_analyze):
    """A simple for-loop to loop over a data construct.

    Args:
        str: A required string.
    Returns:
        tup: Returns a tuple with maximum, minimum and average words.

    Example:
    >>> lexicographics('''Don't stop believing,
    Hold on to that feeling.''')
    (5, 3, Decimal('4'))

    >>> lexicographics('''I am a test string;
    I continue on the next line.''')
    (6, 5, Decimal('5.5'))

    """
    lines = to_analyze.splitlines()
    var = []
    for items in lines:
        var.append(len(items.split()))
    return (max(var), min(var), decimal.Decimal(sum(var))/len(lines))
