# 1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს 
# და დააბრუნებს ამ რიცხვებს შორის შესრულებული არითმეტიკული ოპერაციების შედეგებს 
# (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება).

num_1 = eval(input("Enter first number: "))
num_2 = eval(input("Enter second number: "))

print( f"{num_1} + {num_2} = {num_1 + num_2}")
print( f"{num_1} - {num_2} = {num_1 - num_2}")
print( f"{num_1} * {num_2} = {num_1 * num_2}")
print( f"{num_1} ** {num_2} = {num_1 ** num_2}")
print( f"{num_1} / {num_2} = {num_1 / num_2}")
print( f"{num_1} // {num_2} = {num_1 // num_2}")