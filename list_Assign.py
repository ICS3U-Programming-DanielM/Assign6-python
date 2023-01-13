# This program finds the product of
# all numbers in an array, it then
# splits this array in half.
import constants


# function to split the array
def split_list(original_array, first_array, second_array):
    # find range of each half
    range_loop = len(original_array)
    range_loop = range_loop / 2
    # round range
    range_loop = round(range_loop)
    # first half
    for counter in range(range_loop):
        first_array.append(original_array[counter])
    # second half
    for counter2 in range(range_loop):
        # to avoid an out of range error
        try:
            second_array.append(original_array[(counter2 + range_loop)])
        except Exception:
            break


# function to find product of array
def find_product(array):
    # declare product
    product = 1
    # find range
    range_loop = len(array)
    # loop to find product
    for counter in range(range_loop):
        product = product * array[counter]
    # return answer to main
    return product


def main():
    # declare arrays
    num_list = []
    arr1 = []
    arr2 = []
    # declare counter for do while loop
    counter = 0
    # loop to get input
    while True:
        input_string = input("Enter a number: ")
        try:
            input_float = float(input_string)
            num_list.append(input_float)
            counter = counter + 1
        except Exception:
            print("Invalid input, try again.")
            continue
        if counter >= constants.MAX_NUM:
            break
    # call functions
    product_main = find_product(num_list)
    split_list(num_list, arr1, arr2)
    # display both halves of the array
    print("The first half of this list is: {}". format(arr1))
    print("The second half is : {}". format(arr2))
    print("The product is: {}". format(product_main))


if __name__ == "__main__":
    main()
