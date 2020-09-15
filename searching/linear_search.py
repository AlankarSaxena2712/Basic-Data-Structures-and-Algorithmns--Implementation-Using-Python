def linear_search(array, to_be_found):
    result = False
    for i in array:
        if i == to_be_found:
            result = True
            return result
        else:
            result = False

if __name__ == "__main__":
    array = [2, 5, 7, 8, 4, 9, 1, 3, 0, 6]
    to_be_found = int(input("Enter the element to be searched : "))
    founded = linear_search(array, to_be_found) # This function will return a boolean value whether the element is found or not.
    if founded:
        print("Element founded")
    else:
        print("Element not founded")