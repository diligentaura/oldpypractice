class Person():
    name = height = dateOfBirth = gender = 0
person1 = Person()
person1.name = "Jane Doe"
person1.yearborn = "March 17, 2002"
person1.height = "5.5"
gender = "female"

class Phone():
    name = os = brand = 0
phone1 = Phone()
phone1.name = "Pixel XL"
phone1.os = "Android"
phone1.brand = "Google"

class House():
    size = location = price = 0
house1 = House()
house1.size = "3000 sqr ft"
house1.location = "Georgetown"
house1.price = "$850,000"

students = []

class Student():
    sid = avg = 0
student1 = Student()
student1.sid = "CTK"
student1.avg = "92"

student2 = Student()
student2.sid = "CTK"
student2.avg = "90"

students.append (student1)
students.append (student2)

for i in range (len (students)):
    print (students[i].sid)
    print (students[i].avg)

for student in students:
    print (student.sid)
    print (student.avg)
