# დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

number = int(input("Please, enter a number: "))

def factorial(number):
    if number < 0:
        print("Please, Enter a positive number")
        number = int(input("Please, enter a number: "))
    res = 1
    for i in range(1, number + 1):
        res *= i
    return res

result = factorial(number)
print(result)
