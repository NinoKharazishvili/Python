# შექმენით ორი კლასი:
# I. Student, ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
# II. Address, ატრიბუტებით: city, street


# Student კლასის address ატრიბუტს მნიშვნელობად უნდა მიანჭოთ Address კლასის ეგზემპლარი.

# შექმენთ ორივე კლასის რამდენინე ეგზემპლარი.

# json მოდულის დახმარებით ფაილში შეინახეთ სტუდენტები.

# მოახდინეთ წაკითხვა. შეცვალეთ ატრიბუტ(ებ)ის მნიშვნელობა (მაგ.mark, str), 
# დაამატეთ ახალი ატრიბუტი grade მნიშვნელობით A, B, C, D (A -> [91-100], B -> [81-90], C -> [71-80], D -> <=70).

# შეცვლილი მონაცემები შეინახეთ ფაილში.



import json

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Student:
    row_id = 0
    
    def __init__(self, name, mark, address):
        self.name = name
        self.mark = mark
        self.address = address
        Student.row_id += 1
        self.row_id = Student.row_id
        self.grade = self.calculate_grade()
    
    def calculate_grade(self):
        if self.mark >= 91:
            return "A"
        elif self.mark >= 81:
            return "B"
        elif self.mark >= 71:
            return "C"
        else:
            return "D"

class StudentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                "row_id": obj.row_id,
                "name": obj.name,
                "mark": obj.mark,
                "address": {
                    "city": obj.address.city,
                    "street": obj.address.street
                },
                "grade": obj.grade
            }
        return json.JSONEncoder.default(self, obj)



address1 = Address("Tbilisi", "Saburtalo")
address2 = Address("Tbilisi", "Gldani-7-11-4-93")
address3 = Address("Tbilisi", "Leselidzs str. 25")
address4 = Address("Tbilisi", "Varketili IV 407-5-123")



student1 = Student("Paata", 87, address1)
student2 = Student("Demetre", 100, address2)
student3 = Student("Alexander", 100, address2)
student4 = Student("Teona", 92, address2)
student5 = Student("Nino", 99, address3)
student6 = Student("Andria", 87, address4)


students = [student1, student2, student3, student4, student5, student6]

with open("students.json", "w") as file:
    json.dump(students, file, cls=StudentEncoder, indent=2)


with open("students.json", "r") as file:
    data = json.load(file)


for student in data:
    if "mark" in student:
        student["mark"] = str(student["mark"])
    student["grade"] = student.pop("grade", None)


with open("students.json", "w") as file:
    json.dump(data, file, indent=2)
