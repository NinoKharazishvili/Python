# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები. 
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით).
# მაგ.: race და care ანაგრამებია.

text1 = input("Please, enter a first word: ")
text2 = input("Please, enter a second word: ")

def anagrams(text1, text2):
    text1 = ' '.join(text1.split()).lower()
    text2 = ' '.join(text2.split()).lower()

    sort_text1 = sorted(text1)
    sort_text2 = sorted(text2)

    if sort_text1 == sort_text2:
        return "it is an anagram"
    else:
        return "it is not an anagram"
    
result = anagrams(text1, text2)
print(result)