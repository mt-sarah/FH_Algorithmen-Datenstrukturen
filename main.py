# Exercise 1

def name_age():
    name = input("Name: ")
    age = input("Age: ")
    print("Hello {0}. Your age is: {1}".format(name, age))
    result = name + age
    return result


# print(name_age())

# Exercise 2

def swap_integers(num1, num2):
    x = num1
    y = num2
    print("x = {0}".format(x))
    print("y = {0}".format(y))
    temp = x
    x = y
    y = temp
    print("post swap magic: ")
    print("x = {0}".format(x))
    print("y = {0}".format(y))
    return "{0}{1}".format(x, y)


# print(swap_integers(10, 20))

# Exercise 3

def check_numbers(num1, num2):
    if (num1 and num2) % 10 == 0:
        if (num1 or num2) % 6 == 0:
            return True
    else:
        return False

    # alternative solution which is shorter but way harder to read:
    # return True if (num1 and num2) % 10 == 0 and (num1 or num2) % 6 == 0 else False


# print(check_numbers(60, 30))


# Exercise 4

def sum_up(num1, num2):
    if 0 < num1 < num2:
        my_sum = 0
        while num1 <= num2:
            my_sum += num1
            num1 += 1
            return my_sum
    else:
        return 0


# print(sum_up(1, 3))

# Exercise 5

def circle_area(r1, r2, r3):
    def area(r):
        return 3.14 * r ** 2

    return area(r1) + area(r2) + area(r3)


# print(circle_area(1, 2, 3))


# Exercise 6

def check_string(text):
    return text.casefold().startswith("a") or text.casefold().endswith("a")


# print(check_string("jdklajljldjA"))


# Exercise 7

def triangle(rows):
    row = 1
    while row <= rows:
        star = 1
        while star <= row:
            print("*", end=" ")
            star += 1
        print()
        row += 1

# print(triangle(4))
