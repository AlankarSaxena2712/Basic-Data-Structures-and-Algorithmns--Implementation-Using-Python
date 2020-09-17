def insertionSort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array

if __name__ == "__main__":
    array = [4, 5, 8, 2, 3, 9, 8, 10, 6, 1]
    sorted_array = insertionSort(array, len(array))
    for i in sorted_array:
        print(i, end = "  ")