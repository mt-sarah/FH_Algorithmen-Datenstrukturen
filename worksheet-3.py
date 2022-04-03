def count_vowels(text):
    count = 0
    if isinstance(text, str):
        for character in text.lower():
            if character in 'aeiou':
                count += 1
    else:
        count = 42

    return count


def hamming(text1, text2):
    distance = 0
    index = 0
    if len(text1) == len(text2):
        while (index < len(text1)):
            if(text1[index] != text2[index]):
                distance += 1
            index += 1
    return distance


class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)



class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return self.name + ", " + self.author


class BookShelf:
    def add_book_list(self, books):
        self.books = books


