# # davaleba - 1
#დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
#მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands: append, remove, exit


arr = []

while True:
    command = input("Enter a command: \n a -> add a number \n r -> remove a number \n e -> exit: \n ")

    if command == 'a':
        input_a = eval(input("Enter a number: "))
        arr.append(input_a)
        print(arr)
    elif command == 'r':
        input_r = eval(input("Enter a number to remove: "))
        arr.remove(input_r)
        print(arr)
    elif command == 'e':
        break
    else:
        print("Invalid command. Please enter 'a', 'r', or 'e'.")

print("Final list:", arr)

###################################################################################

# davaleba - 2
#დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
#a. დაბეჭდავს 210-ის ინდექსს;
#b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
#c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
#d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

my_list = [43, '22', 12, 66, 210, ["hi"]]
my_llist_2 = my_list.copy()

print(my_list.index(210))

for item in my_list:
    if type(item) == list:
        item.append("Hello")

popped_element = my_list.pop(2)
print(my_list)

print(my_llist_2)
my_llist_2.clear()
print(my_list, "\n", my_llist_2)

####################################################################################
# davaleba - 3 
#დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, 
#თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, 
#წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

import re

number = input("Enter your phone number: ")

pattern = r"\(123\) \d{3}-\d{3}"

if re.match(pattern, number):
    print(number)
else:
    print("Invalid format")

