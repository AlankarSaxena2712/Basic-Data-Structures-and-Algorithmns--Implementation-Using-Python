def selectionSort(array, n):
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array

if __name__ == "__main__":
    array = [2, 5, 12, 4, 8, 10, 1, 9, 3, 11, 7, 6]
    sorted_array = selectionSort(array, len(array))
    for i in sorted_array:
        print(i, end = "  ")