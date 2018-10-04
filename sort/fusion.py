

def fusion(lst):
    buffer = lst[:]
    _fusion(lst, buffer, 0, len(lst))
    return lst


def _fusion(lst, buffer, start, end):
    if end - start <= 1:
        return
    median = (start + end) // 2
    _fusion(buffer, lst, start, median)
    _fusion(buffer, lst, median, end)
    merge(lst, buffer, start, median, end)


def merge(lst, buffer, start, median, end):
    x = start
    y = median
    for i in range(start, end):
        if y >= end or (x < median and buffer[x] < buffer[y]):
            lst[i] = buffer[x]
            x += 1
        else:
            lst[i] = buffer[y]
            y += 1
