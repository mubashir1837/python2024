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

class Prices:
    def __init__(self, tomato, potato, carrot, mango, apple ):
        print("prices:")
        self.tomato = tomato
        self.potato = potato
        self.carrot = carrot
        self.mango = mango
        self.apple = apple

january = Prices(500, 400, 350, 244, 600)
print(january.tomato, january.potato, january.carrot, january.mango, january.apple)

feb = Prices(450, 500, 300, 670, 455)
print(feb.tomato, feb.potato, feb.carrot, feb.mango, feb.apple )

Mar =Prices(677, 455, 433, 800, 566)
print(Mar.tomato, Mar.potato, Mar.carrot, Mar.mango, Mar.apple)

Apr = Prices(555, 600, 670 ,300, 654)
print(Apr.tomato, Apr.potato, Apr.carrot, Apr.mango, Apr.apple)

May =Prices(500, 560, 670, 300, 450)
print(May.tomato, May. potato, May.carrot, May.mango, May.apple)

June =Prices(300, 450, 333, 556, 880)
print(June.tomato, June.potato, June.carrot, June.mango, June.apple)

July =Prices(600, 456, 300, 670 ,566)
print(July.tomato, July.potato, July.carrot, July.mango, July.apple)


class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account


    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debitted")
        print("total balance=", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs,", amount, "was creditted")
        print ("total balanace =", self.get_balance())


    def get_balance(self):
        return self.balance



account1 =Account(1999, 3000 )
account1.debit(1000)
account1.credit(50550)
account1.credit(555000)

