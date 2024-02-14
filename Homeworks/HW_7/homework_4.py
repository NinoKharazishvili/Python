# დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.

text = input("Please, enter a string: ")
symbo = input("Please, enter one symbol: ")

def check(text, symbo):
    sum = 0
    for i in text:
        if i.lower() == symbo.lower():
            sum += 1
    return sum


result = check(text, symbo)
print(f"The character '{symbo}' appears {result} times in the string.")
