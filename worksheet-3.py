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
    def __init__(self):
        self.books = []

    def add_book_list(self, new_books):
        for i in new_books:
            if isinstance(i, Book):
                self.books.append(i)

    def books_by_author(self, author):
        book_names = []
        for i in self.books:
            if i.author == author:
                book_names.append(i.name)
        return book_names

    def get_books(self):
        book_names = []
        for i in self.books:
            book_names.append(i.name)
        return book_names

    def clear_shelf(self):
        self.books.clear()


# book1 = Book("Harry Potter 1", "JK Rowling")
# book2 = Book("Harry Potter 2", "JK Rowling")
# book3 = Book("Harry Potter 3", "JK Rowling")
# book4 = Book("Harry Potter 4", "JK Rowling")
# book5 = Book("Lord of the Rings 1", "JRR Tolkien")
# book6 = Book("Lord of the Rings 2", "JRR Tolkien")
# book7 = Book("Lord of the Rings 3", "JRR Tolkien")
# # book8 = Book("Good Omens")
# book9 = ["American Gods", "Neil Gaiman"]
# book10 = 42
#

# my_book_list = [book1, book2, book5, book7]
#
# my_shelf = BookShelf()
#
# my_shelf.add_book_list(my_book_list)

# my_sorted_shelf = my_shelf.books_by_author("JK Rowling")
# print(my_sorted_shelf)
# print(my_shelf.books_by_author("JK Rowling"))
# print(my_shelf.get_books())
#
# my_shelf.clear_shelf()
# # my_sorted_shelf.clear_shelf()
# print(my_sorted_shelf)
# print(my_shelf.books_by_author("JK Rowling"))
