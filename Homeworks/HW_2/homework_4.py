#შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
#თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
#თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
#სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
#რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = int(input("Enter a number: "))

if num > num_list[2] and num < num_list[-1]:
    print("More than list elements")
elif num == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")