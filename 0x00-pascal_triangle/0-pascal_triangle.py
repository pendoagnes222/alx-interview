#!/usr/bin/python3

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
         n: number of pascal triangle 
    """
    output = [[] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    output[i].append(1)
                else:
                    output[i].append(output[i - 1][j - 1] + output[i - 1][j])
            elif (j == i):
                output[i].append(1)
    return output
