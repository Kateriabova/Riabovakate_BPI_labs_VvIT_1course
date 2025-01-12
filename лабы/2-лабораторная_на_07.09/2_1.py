def greet(name):
    print(f"Добрейший вечерочек, {name}! Как поживаете?")

def square(number):
    return number * number

def max_of_two(x, y):
    m = x
    if y > m:
        m = y
    return m

greet('Анна-Мария')
a = square(3)
print(a)
print(max_of_two(a, 34))

