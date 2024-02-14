#2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). 
#კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
#ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

#მაგალითად:
#book1 = Book('1984', 'George Orwell')
#book2 = Book('1984', 'George Orwell')
#book3 = Book('Brave New World', 'Aldous Huxley')
#print(book1 == book2)  # Output: True
#print(book1 == book3)  # Output: False


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

#-------------------------------------------#
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2) 
print(book1 == book3) 
