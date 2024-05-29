"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def shuffler():
    s = "manjeet"
    r = len(s) - 1
    order = list(s)
    for l in range(len(s) // 2):
        [order[l], order[r]] = [order[r], order[l]]
        r -= 1
    print(''.join(order))

shuffler()
