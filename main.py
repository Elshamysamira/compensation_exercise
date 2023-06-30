# Exercise 1:
def calc_average(numbers: list):
    total_sum = 0
    count = 0

    for num in numbers:
        if not isinstance(num, int):
            raise ValueError('Invalid value in the list')

        total_sum += num
        count += 1

    if count == 0:
        return 0

    average = total_sum / count
    return average


# Exercise 2:
def print_pyramid(rows: int):
    if not isinstance(rows, int):
        raise ValueError('Invalid value for rows')
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))


# Exercise 3:
def clean_string(my_string: str):
    cleaned_string = ""
    for char in my_string:
        if char.isalpha() or char.isspace():
            cleaned_string += char
    return cleaned_string


# Exercise 4:
def count_special_char(my_string: str):
    count = 0
    for char in my_string:
        if not char.isalpha() and not char.isspace():
            count += 1
    return count


# Exercise 5:
def dict_to_list(dictionary: dict):
    if not dictionary:
        return []
    return list(dictionary.values())


# Exercise 6:
def list_to_dict(key_list: list, value_list: list):
    if len(key_list) != len(value_list):
        raise ValueError('Lists must be of the same length')
    return dict(zip(key_list, value_list))


# Exercise 7:
def chunk_list(my_list: list, chunks: int):
    if len(my_list) == 0:
        raise ValueError('The list must not be empty')
    if len(my_list) % chunks != 0:
        raise ValueError('The list length must be divisible by chunk size')
    chunk_size = len(my_list) // chunks
    chunked_list = []
    for i in range(0, len(my_list), chunk_size):
        chunked_list.append(my_list[i : i + chunk_size])
    return chunked_list


# Exercise 8:
class Book:
    def __init__(self, name, author, genre, borrowed=False):
        self.name = name
        self.author = author
        self.genre = genre
        self.borrowed = borrowed

    def __str__(self):
        return f"{self.name}, {self.author}, {'True' if self.borrowed else 'False'}"


# Exercise 9
class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.book_list.append(book)

    def get_all_books(self):
        if any(self.book_list):
            return self.book_list
        else:
            return []

    def borrow_book(self, book):
        if isinstance(book, Book):
            if book not in self.book_list:
                print("Book does not exist")
            if book in self.book_list:
                if book.borrowed is True:
                    print("Book already borrowed")
                book.borrowed = True

    def return_book(self, book):
        if isinstance(book, Book):
            if book not in self.book_list:
                print("Book does not exist")
            if book in self.book_list:
                if book.borrowed is False:
                    print("Book has not been borrowed")
                book.borrowed = False


# Exercise 10
class BookStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        if isinstance(book, Book):
            self.stack.append(book)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Exercise 11:
def count_words(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()
        word_count = len(content.split())
        return word_count


# Exercise 12:
def count_lines(file_path: str):
    with open(file_path, "r") as file:
        content = file.read()
        line_count = len(content.split("\n"))
        return line_count


# Exercise 13:
def write_even(input_file_path: str, output_file_path):
    with open(input_file_path, "r") as file:
        lines = file.readlines()
        second_lines = lines[1::2]

    with open(output_file_path, "w") as file:
        file.writelines(second_lines)
