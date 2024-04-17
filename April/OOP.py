#Objects oriented programming.
class Student:
    name ="arjun"


s1 = Student
print(s1.name)

s2 = Student()
print(s2.name)



class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)


class Google:
    color ="bryg"
    spell ="google"

g1 = Google()
print(g1.color)
print(g1.spell)



class Fruits:
    apple ="Red"
    mango ="Yellow"

fruits1 = Fruits()
print(fruits1.apple)
print(fruits1.mango)



class Fruit:
    taste = "sweet"
    color = "Yellow"

fruit1 = Fruit()
print(fruit1.taste)
print(fruit1.color)


class Vegetable:
    color = "red"
    shape = "round"

vegetable1 = Vegetable()
print(vegetable1.color)
print(vegetable1.shape)



class Mobile:
    name = "OPPO"
    version = "2024"

mobile1 = Mobile()
print(mobile1.name)
print(mobile1.version)



class Laptops:
    name1 = "hp"
    name2 = "dell"

laptop1 =Laptops()
print(laptop1.name1)
print(laptop1.name2)


class car:
    def getSpeed(self):
        print("155 mph")

BMW = car()
FORD = car()
car.getSpeed(BMW)
car.getSpeed(FORD)

BMW.getSpeed()
FORD.getSpeed()



class University:
    def students(present):
        print("50P")

FRI = University()
SAT =University()
University.students(FRI)
University.students(SAT)



class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in class")

s1 = Student("arjun")
print(s1.name)
s2 = Student("Karan")
print(s2.name)
s3 =Student("Mubashir")
print(s3.name)
s4 =Student("Sadaqat")
print(s4.name)
s5 =Student("Danish")
print(s5.name)
s6 = Student("Saleem")
print(s6.name)




class Students:
    def __init__(self, marks, subjects, names):
        self.marks = marks
        self.subjects =subjects
        self.names =names
        print("Adding marks and subjects...")

ms1 = Students(23,"Biology", "Karan")
print(ms1.marks, ms1.subjects, ms1.names)
ms2 = Students(50, "Chemistry", "Arjun")
print(ms2.marks, ms2.subjects, ms1.names)
ms3 = Students(46, "Physics", "Sadia")
print(ms3.marks, ms3.subjects, ms3.names)
ms4 = Students(45, "English", "Sajjida")
print(ms4.marks, ms4.subjects, ms4.names)
ms5 = Students(48,"Urdu", "Touqeer")
print(ms5.marks, ms5.subjects, ms5.names)




class Bike:
    def __init__(self,brands,Color, price, length, height):
        self.brands = brands
        self.color = Color
        self.price = price
        self.length = length
        self.height = height

data1 = Bike("new", "red", "1lac", 134, 4)
print(data1.brands, data1.color, data1.price, data1.length, data1.height)
data2 = Bike("new", "Yellow", "1.5lac", 132, 4)
print(data2.brands, data2.color, data2.price, data2.length, data2.height)
data3 = Bike("new", "blue", "1.5lac", 130, 5)
print(data3.brands, data3.color, data3.price, data3.length, data3.height)


class Car:
    def __init__(self,price, brand, color, model):
        self.price = price
        self.brand = brand
        self.color = color
        self.model = model
car1 =Car("1 crore", "new", "white", "2024")
print(car1.price, car1.brand, car1.color, car1.model)
car2 =Car("2 crore", "new", "white", "2024")
print(car2.price, car2.brand, car2.color, car2.model)
car3 = Car("1.5 crore", "new", "black", "2025")
print(car3.price, car3.brand, car3.color, car3.model)


class House:
    def __init__(self, area, type, color, place):
        self.area = area
        self.type = type
        self.color = color
        self.place = place
House1 = House("2kanal", "Double", "color", "place")
print(House1.area, House1.type, House1.color, House1.place)


        



class Person:
    name =  "MUbashir"
    occ = "Student"

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person()
print(a.name)
#change
a.name = "Ali"
a.name = "Hussain"
a.name = "Sadaqat"
#OR
a.info()
b = Person()
print(b.occ)
#To change
b.occ = "Teacher"
b.occ = "Captain"
#OR
b.info()


