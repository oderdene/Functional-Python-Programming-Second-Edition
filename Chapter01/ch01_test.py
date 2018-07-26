#!/usr/bin/env python3

def test(b,k):
    """
    >>> test()
    23

    """

    s = 0
    for n in range(1, 10):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    print(s)


if __name__ == "__main__":
    # test()
    print(test.__code__.co_varnames)
    print(test.__code__.co_argcount)