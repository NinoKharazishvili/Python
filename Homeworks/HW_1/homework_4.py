#4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

height = eval(input("Enter the height of the triangle: "))
base = eval(input("Enter the length of the base of the triangle: "))

area = int((height * base) / 2)
print("The area of the triangle is", area)