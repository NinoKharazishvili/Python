# davaleba - 1
#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

#n-მდე რიცხვების ჯამი:
n = int(input("Enter a number: "))
sum = 0

for i in range (1, n):
    sum += i

print(sum)

##########
#n-ის ჩათვლით რიცხვების ჯამი:
n = int(input("Enter a number: "))
sum = 0

for i in range (1, n +1 ):
    sum += i

print(sum)

################################################################################

# davaleba - 2
#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. 
#მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1

num = int(input("Enter a number: "))

while num >= 1:
    print(num, end=' ')
    num -= 1

#################################################################################

# davaleba - 3
#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. 
#მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1

from random import randint

x = randint(1, 100)

while True:
    num = int(input("Guess the number: "))
    if num == x:
        print("Correct! Congratulations! You guessed the correct number.")
        break
    if num < x:
        print("too low")
    if num > x:
        print("too high")

##################################################################################

# davaleba - 4
#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, 
#შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. 
#ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

total_sum = 0

while True:
    user_input = input("Enter a number (type 'sum' to finish): ")
    if user_input == "sum":
        break
    if eval(user_input) > 0:
        total_sum += eval(user_input)
    else:
        print("Enter a positive number!")

print(f"total sum is {total_sum}")
