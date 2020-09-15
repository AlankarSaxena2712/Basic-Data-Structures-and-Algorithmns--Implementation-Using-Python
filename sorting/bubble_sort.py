def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

if __name__ == "__main__":
    array = [4, 5, 8, 2, 3, 9, 8, 10, 6, 1]
    sorted_array = bubbleSort(array)
    for i in sorted_array:
        print(i, end = "  ")