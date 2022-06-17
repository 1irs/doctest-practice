# Source: http://rosettacode.org/
import doctest


def bubble_sort(seq):
    """
    Put your doctests here:

    >>> bubble_sort([])
    []

    """
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq


doctest.testmod(verbose=True)
