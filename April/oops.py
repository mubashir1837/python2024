class Student:

    def __init__(self, name, rollno, marks ):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        print ("new students")

s1 = Student("Mubashir", 25, 1047)
print(s1.name, s1.rollno, s1.marks)

class Subjects:
    def __init__(self, phy, chem, bio, math, urdu, eng):
        print("marks of student :")
        self.phy =phy
        self.chem =chem
        self.bio= bio
        self.math = math
        self.urdu = urdu
        self.eng = eng

Ahmed = Subjects(25, 55, 60, 75, 100, 76)
print(Ahmed.phy, Ahmed.chem, Ahmed.bio, Ahmed.math, Ahmed.urdu, Ahmed.eng )

Ali = Subjects(40, 60, 70, 92, 10, 45)
print(Ali.phy, Ali.chem, Ali.bio, Ali.math, Ali.urdu, Ali.eng)

Saif = Subjects(45,56,78,35,45,100)
print(Saif.phy, Saif.chem, Saif.bio, Saif.math, Saif.urdu, Saif.eng)

Asim = Subjects(60,45,98,66,100,46)
print(Asim.phy, Asim.chem, Asim.bio, Asim.math, Asim.urdu, Asim.eng)

Anil =Subjects(45,67, 55, 54, 100, 54)
print(Anil.phy, Anil.chem, Anil.bio, Anil.math, Anil.urdu, Anil.eng)

Abid =Subjects(43, 100, 65, 67, 45, 78)
print(Abid.phy, Abid.chem, Abid.bio, Abid.math, Abid.urdu, Abid.eng)


        