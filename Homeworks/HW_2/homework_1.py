#შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], 
#in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = int(input("Enter a number: "))

if num in num_list:
    print("The number in list")
else:
    print("The number not in list")