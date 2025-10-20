def find_largest_number(numbers_list):

    # Base case - only item in the last will be the largest
    if len(numbers_list) == 1:
        return numbers_list[0]

    # Comparing the first and last item
    if numbers_list[0] > numbers_list[-1]:
        # Call function but without the last item
        return find_largest_number(numbers_list[0:-1])
    else:
        # Call function but without the first item
        return find_largest_number(numbers_list[1:])


# Print output
print(f"Largest number: {find_largest_number([10, 99, 1, 22, 666, 2, 40])}")
