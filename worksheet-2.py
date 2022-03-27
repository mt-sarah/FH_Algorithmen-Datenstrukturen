def count_integers(numbers, integer):
    count = 0
    for i in numbers:
        if i == integer:
            count += 1
    if count > 1:
        return count
    else:
        return 42


# I'm assuming that I should still print the reversed list even if the integer does not occur in the list
def list_func(numbers, integer):
    def print_reverse_numbers():
        temp_numbers = numbers.copy()
        temp_numbers.reverse()
        print(temp_numbers)
    if integer in numbers:
        for index, value in enumerate(numbers):
            numbers[index] = 6 if value == integer else value
        print_reverse_numbers()
    else:
        print_reverse_numbers()
        numbers.clear()

    return numbers


def compare_lists(list1, list2):
    new_list = []
    # easy option:
    # new_list = list(set(list1).intersection(list2))
    # another easy option:
    # new_list = [i for i in list1 if i in list2]
    for i in list1:
        if i in list2:
            new_list += [i]
            # or
            # new_list.append(i)
    return new_list


def remove_duplicates(lst):
    # for keeping the original order:
    new_list = list(dict.fromkeys(lst))
    # alternative if the order doesn't matter
    # new_list = list(set(lst))
    return new_list


def dict_func(dictionary):
    my_type = dictionary.get('Type', "unknown type")
    brand = dictionary.get("Brand", "unknown brand")
    price = dictionary.get("Price", "unknown price")
    dictionary['OS'] = 'Linux'
    print("YOU HAVE A {0} from {1} that costs {2}".format(
        my_type, brand, price))
    return dictionary
