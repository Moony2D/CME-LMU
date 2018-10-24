def same_start_and_end(seq):
    """ (array) -> bool

    Precondition: len(seq) != 0

    Return whether an array starts and ends with the same value.

    >>> s = 'abracadabra'
    >>> same_start_and_end(s)
    True
    >>> s = [1,2,3]
    >>> same_start_and_end(s)
    True
    """

    return seq[0] == seq[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()