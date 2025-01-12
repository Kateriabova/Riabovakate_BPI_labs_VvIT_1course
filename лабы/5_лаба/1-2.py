class Book:
    title = 'The Gray House'
    author = 'Mariam Petrosyan'
    year = '2017'
    count = 0

    def __init__(self):
        Book.count += 1

    def get_info(self):
        print(f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}')

class Circle:
    def __init__(self, rad):
        self.radius = rad

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

b = Book()
b.get_info()
print(b.count)
b_2 = Book()
print(b_2.count)
cruzhochek = Circle(5)
print(cruzhochek.get_radius())
cruzhochek.set_radius(90)
print(cruzhochek.get_radius())