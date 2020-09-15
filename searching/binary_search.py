def binary_search(array, to_be_found):
    f = 0
    e = len(array) - 1
    while f <= e:
        mid = int((f + e) / 2)
        if to_be_found == array[mid]:
            return True
        elif to_be_found < array[mid]:
            e = mid - 1
        else:
            f = mid + 1

if __name__ == "__main__":
    array = [2, 5, 7, 8, 4, 9, 1, 3, 0, 6]
    to_be_found = int(input("Enter the element to be searched : "))
    founded = binary_search(array, to_be_found) # This function will return a boolean value whether the element is found or not.
    if founded:
        print("Element founded")
    else:
        print("Element not founded")