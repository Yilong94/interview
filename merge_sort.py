def mergeSort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    sortedLeft = mergeSort(arr[0:middle])
    sortedRight = mergeSort(arr[middle:])
    return merge(sortedLeft, sortedRight)


def merge(arr1, arr2):
    arr = []
    p1 = 0
    p2 = 0

    while True:
        # if pointer has reached end of an array, append the rest for other array
        # since it is guaranteed that the rest will be more than the last item in former array
        if p1 >= len(arr1):
            arr.extend(arr2[p2:])
            break

        if p2 >= len(arr2):
            arr.extend(arr1[p1:])
            break

        if arr1[p1] < arr2[p2]:
            arr.append(arr1[p1])
            p1 += 1
        else:
            arr.append(arr2[p2])
            p2 += 1

    return arr
