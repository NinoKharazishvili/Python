# davaleba - 1
#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

text = input("Please, enter a text: ")

print(text.encode('utf-8'))

##########################################################
#davaleba - 2
#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. 
#ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'. 
#თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
#მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip().

text = input("Please, enter a text: ")
text1 = ' '.join(text.split()).lower() 

if 'python' in text1:
    text2 = text1.replace("python", "Python")

print(text2 + " Python")

#############################################################
#davaleba - 3
#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

text = input("Please, enter a text: ")
half = text[:len(text) // 2]
print("First half of the text is:", half)


#############################################################
# davaleba - 4
#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. 
#სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)
import string

text = input("Please, enter a text: ")

digits = string.digits
letters = string.ascii_letters
digits_letters = digits + letters

digit = any(ch in digits for ch in text)
letter = any(ch in letters for ch in text)
is_valid = all(ch in digits_letters for ch in text)

if is_valid and digit and letter:
    print("Text is valid")
else:
    print("Text isn't valid")


##############################################################
# davaleba - 5
#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, 
#ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.
    
text = input("Please, enter a text: ")
text = text.encode('utf-8')
print("Bytes representation:", text)
 
text = text.decode('utf-8')
print("Decoded string:", text)