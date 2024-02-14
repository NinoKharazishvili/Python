#2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

diagonal_1 = eval(input("Enter the length of the first diagonal: "))
diagonal_2 = eval(input("Enter the length of the second diagonal: "))

rhombus_area = int((diagonal_1 * diagonal_2) / 2)
print("The area of the rhombus is", rhombus_area)
