def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    step = 0

    while start <= end:
        print("step: ", step, ":", str(list[start:end + 1]))

        step = step + 1
        middle = (start + end) // 2

        if middle == element:
            return middle
        elif middle > element:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1

binary_search(my_list, target)
