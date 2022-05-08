def power(a, b):
    if b == 0:
        return 1
    elif a < 0 or b < 0:
        return -1

    else:
        return a * power(a, b-1)


# print(power(2, 4))


def binary_search(numbers, num, start, end):
    # returns -1 if the start number is higher than the end number - base case
    if start > end:
        return -1

    # finds the index that's right in the middle of the list by adding up starting and ending index and dividing by two
    # the // operator divides, rounds down and returns whole number
    middle = (start+end) // 2
    if num == numbers[middle]:
        return middle  # returns the middle if the searched int is exactly that
    if num < numbers[middle]:  # if the searched int is lower, checks the left part
        # end is adapted to middle -1
        return binary_search(numbers, num, start, middle-1)
    else:  # if the searched int is higher, checks the right part and the starting point is middle +1
        return binary_search(numbers, num, middle+1, end)
    # if the number can't be found, the recursion unfolds to the base case in the else statement and returns -1

# numbers = [1, 3, 9, 14, 16, 18, 40, 66, 71]

# print(binary_search(numbers, 30, 1, 6))


class HashTable:
    def __init__(self, size):
        self.size = size
        self.list = [[] for x in range(self.size)]

    def __my_hash(self, element):
        if type(element) is str:
            key = 0
            for char in element:
                key += ord(char)
            return key % self.size
        elif type(element) is int:
            return element % self.size

    def insert(self, element):
        key = self.__my_hash(element)
        self.list[key].append(element)

    def get_element(self, element):
        key = self.__my_hash(element)
        if len(self.list[key]) == 0:
            return False
        else:
            if element in self.list:
                return self.list[key].remove(element)
            else:
                return False

    def get_size(self):
        length = 0
        for key in range(self.size):
            if len(self.list[key]) == 0:
                length += 1
            else:
                length += len(self.list[key])

        return length


# newHashTable = HashTable(10)
# newHashTable.insert("mouse")
# newHashTable.insert("cat")
# newHashTable.insert("dog")
# newHashTable.insert(9)
# newHashTable.insert(42)
# newHashTable.insert("bla")
# print(newHashTable.get_element(9))
# print(newHashTable.get_size())

# print(newHashTable.list)
