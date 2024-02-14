##davaleba 1
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


##############################################################################################################################################

# #davaleba 2
#2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

diagonal_1 = eval(input("Enter the length of the first diagonal: "))
diagonal_2 = eval(input("Enter the length of the second diagonal: "))

rhombus_area = int((diagonal_1 * diagonal_2) / 2)
print("The area of the rhombus is", rhombus_area)


################################################################################################################################################

# #davaleba 3
#3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში

meter = eval(input("Enter in meters: "))

centimeter = meter * 100
decimeter = meter * 10
millimeter = meter * 1000
mile = meter / 1609.344

print (meter, "meters is", centimeter, "centimeters")
print (meter, "meters is", decimeter, "decimeters")
print (meter, "meters is", millimeter, "millimeters")
print (meter, "meters is", mile, "miles")


#################################################################################################################################################

#davaleba 4
#4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

height = eval(input("Enter the height of the triangle: "))
base = eval(input("Enter the length of the base of the triangle: "))

area = int((height * base) / 2)
print("The area of the triangle is", area)