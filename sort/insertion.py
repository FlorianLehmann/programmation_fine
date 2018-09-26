def insertion(numbers):
    for i in range(1,len(numbers)):
        tmp = i
        for j in reversed(range(0,i)):
            if numbers[tmp] >= numbers[j]:
                break
            else:
                numbers[tmp], numbers[j] = numbers[j], numbers[tmp]
                tmp = tmp - 1

