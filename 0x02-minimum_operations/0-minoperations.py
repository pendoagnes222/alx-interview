#!/usr/bin/python3


def minOperations(n):
    curr = 1
    prev = 0
    count = 0

    while (curr < n):
        empty_position = n - curr

        if (empty_position % curr == 0):
            prev = curr
            curr += prev
            count += 2
        else:
            curr += prev
            count += 1
    return count
