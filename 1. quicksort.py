def partition(array, lowest, highest):
    pivot = array[highest]
    i = lowest - 1

    for j in range(lowest, highest):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[highest] = array[highest], array[i + 1]
    return i + 1

def quicksort(array, lowest, highest):
    if lowest < highest:
        pi = partition(array, lowest, highest)

        quicksort(array, lowest, pi - 1)
        quicksort(array, pi + 1, highest)

def statistic(array, lowest, highest, i):
    if lowest < highest:
        pi = partition(array, lowest, highest)

        if pi == i:
            return array[pi]
        elif pi > i:
            return statistic(array, lowest, pi - 1, i)
        else:
            return statistic(array, pi + 1, highest, i - pi - 1)
    else:
        return arr[lowest]


array = [4, 11, 18, 15, 2, 7, 20]
quicksort(array, 0, len(array) - 1)

i = 4  
result = statistic(array, 0, len(array) - 1, i - 1)

print(f"The {i}th smallest position in the sorted array: {result}")


//output: The 4th smallest position in the sorted array: 11
