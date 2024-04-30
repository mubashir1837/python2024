###Sets in python

school = {1 ,2,3,4}
print(school)
print(type(school))

college = {3, 4, 5, 6}
print(college)
print(type(college))

students = {4, 6, 7, 9}
print(students)
print(type(students))

## Empty Set
empty_set =set()
print(type(empty_set))

## SET METHODS
### .add(el) to add an element
set ={"A", "B", "C","D", "E"}
set.add("F")
print(set)

set.add("H")
print(set)

set.add("I")
print(set)
#
Google ={"g","o", "o", "g"}
Google.add("l")
print(Google)

Google.add("e")
print(Google)

Google.add("s")
print(Google)
#
facebook ={"f","a","c","e"}
facebook.add("b")
print(facebook)

facebook.add("o")
print(facebook)

facebook.add("k")
print(facebook)

### .remove(el) # to remove element
instagram ={"i", "n","s","t","a","g", "r", "a","m"}
instagram.remove("g")
print(instagram)

instagram.remove("r")
print(instagram)

instagram.remove("m")
print(instagram)

instagram.remove("s")
print(instagram)

instagram.remove("i")
print(instagram)

instagram.remove("n")
print(instagram)

instagram.remove("a")
print(instagram)


### .clear() #empties set
google = {1,2,3,4,5,6,7,8}
google.clear()
print(google) #set()

facebook = {5,4,3,2,5,5}
facebook.clear()
print(facebook) #set()

instagram = {"i","n","s","t","a","g","r","a","m"}
instagram.clear()
print(instagram) # set()

tiktok ={"t","i","k","t","o","k"}
tiktok.clear()
print(tiktok) # set()

### .pop() removes a random value
google ={1,2,3,5,6,7}
google.pop()
print(google)

facebooks ={"a", "b","c","d","e"}
facebooks.pop()
print(facebooks)

instagrams ={1,4,2,7,8,3}
instagrams.pop()
print(instagrams)


### .union(set2) combines both set values and return new

set1 ={1,2,3}
set2 ={2,3,4}
print(set1.union(set2)) #(1,2,3,4)

books1 = { "Urdu","Eng","Isl"}
books2 = {"Urdu","Phy","chem","Bio"}
print(books1.union(books2))

Google1 = {3,5,4,1,2}
Facebook1 = {9,8,7,6,4,2}
print(Google1.union(Facebook1))

instagram = {6,5,4,3}
youtube = {9,8,7,2,3}
print(instagram.union(youtube))

snapchat ={"a","b","c","d","e"}
whatsapp ={"a","f","g","h","i"}
print(snapchat.union(whatsapp))

skype ={"s","h","a","k"}
twitter ={"h","e","k","l"}
print(skype.union(twitter))

pakistan1 ={"Lahore","Rawalpindi","Karachi","Skardu","Gilgit"}
pakistan2 ={"Multan","Karachi","Hayderabad","Gujaranwala"}
print(pakistan1.union(pakistan2))


a ={1,4,3,2,5,6}
b ={6,7,8,9,3}
print(a.union(b))


### set.intersection(set2) cmbines comman values and returns new
set1 ={6,3,2,4}
set2 ={3,4,5,6}
print(set1.intersection(set2))


GoogleA ={"G","O","A","L","E"}
GoogleB ={"G","O","S","Y","E"}
print(GoogleA.intersection(GoogleB)) ##{"G","E","O"}


Facebookf ={2,3,4,5,12}
Facebookg ={2,3,7,8,9}
print(Facebookf.intersection(Facebookg))


instagramA ={"I","S",'T',"A","G","R","M"}
instagramB={"I","N","S","T","A"}
print(instagramA.intersection(instagramB))

schoolA ={1,2,3,4,5,6}
SchoolB ={3,5,6,7,8}
print(schoolA.intersection(SchoolB))


### Store the following words meanings in python

Dictionary ={
    "cat" : "a small animal",
    "table" : ["a piece of wood","list of facts and figure"]
}
print(Dictionary)



### You are given a list of subjects fir students.Assume one class room is required for 1 subject.How many calssrooms are needed by all students.
subjects ={
    "python","Java","C++","python","javascript","jave"
    "python","Java","C++","c"
}
print(len(subjects))
print(subjects)


#### Que:
marks ={}
x =int(input("enter phy :"))
marks.update({"phy" : x})

x =int(input("enter math :"))
marks.update({"math" : x})

x =int(input("enter chem: "))
marks.update({"chem" : x})

print(marks)


count=1
while count <= 5:
    print("hello")
    count += 1

count = 2
while count <=100:
    print("ATCG")
    count +=2

a = input("Enter your name: ")
print("My name is ", a)

b = input("Enter your age:")
print("My age is ", b)

c = input("Enter you father name:")
print("My father name is ", c)

d  = input("Enter your mother name:")
print("My mother name is ", d)

e = input("Enter your brother name:")
print("My brother name is ", e)

f = input ("Enter your sister name:")
print("My sister name is ", f)

g = input("Enter your best friend name:")
print("My best friend name is ", g)

h = input("Enter your favourite food:")
print("My favourite food is ", h)

i = input("Enter your favourite drink:")
print("My favourite drink is ", i)

j = input("Enter you favourite colour:")
print("My favourite colour is ", j)

k  = input("Enter your favourite sport:")
print("My favourite sport is :", k)

l = input("Enter your favourite subject:")
print("My favourite subject is :", l)

m = input("Enter your favourite subject:")
print("My favourite subject is :", m)

n =  input("Enter you favourite subject:")
print("My favourite subject is :", n)

x = input("Enter first number:")
y = input("Enter second number:")

print(int(x)+ int(y))

name = "harryuuuuu"
friend = "rohan"
anotherfriend = "lovish"
apple = '''He said,'''
print("Hello,"+ name)
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

names = "Mubashir, Mubashir"
print(len(names))
fruits = "Mango", "apple", "banana"
print(len(fruits))
vegetables = "tomato", "potato", "onion"
print(len(vegetables))

vehicles = "car", "bike", "cycle"
print(len(vehicles))

# fruits = "Mango"
a = "Mango"
print(a[0:4])

b = "banana"
print(b[0:4])

c = "apple"
print(c[0:4])

d = "tomato"
print(d[0:4])

f = "potato"
print(f[3:5])

g = "onion"
print(g[0:5])

h = "car"
print(h[0:3])

i = "bicycle"
print(i[0:3])

j = "monkey"
print(m[1:5])


a = "mubashir"
print(len(a))
print(a.upper())

b = "MUBASHIR"
print(len(b))
print(b.lower())

c = "arslaan"
print(len(c))
print(c.upper())

d = "ARSLAAN"
print(len(d))
print(d.lower())

e = "eshrat"
print(len(e))
print(e.upper())

f = "ESHRAT"
print(len(f))
print(f.lower())

g = "maisam"
print(len(g))
print(g.upper())

h = "MAISAIM"
print(len(h))
print(h.lower())

i = "atif"
print(len(i))
print(i.upper())

j = "ATIF"
print(len(j))
print(j.lower())


y = "!!!!mubashir!!!!!"
print(i.rstrip)

z = "!!!!!zahid!!!"
print(z.rstrip)

q = "!!!!!naina!!!!!"
print(q.rstrip)


w = "!!!wahab!!!!!!"
print(w.rstrip)


ahmira  = "amrita"
print(ahmira.capitalize)

amrita = "ahmira"
print(amrita.replace("mubashir", "ahmed"))


a = "amrita"
print(a.count("amrita"))

b = "baloon"
print(b.count("baloon"))



subjects = {"python", "Java", "C++", "python", "javascript", "java", "python", "Java", "C++", "c"}
print(len(subjects))
print(subjects)

# Correction in union() method calls
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))  # {1, 2, 3, 4}

# Correction in storing word meanings in a dictionary
Dictionary = {
    "cat": "a small animal",
    "table": ["a piece of wood", "list of facts and figure"]
}
print(Dictionary)

count = 1
while count <= 5:
    print("hello")
    count += 1

count = 2
while count <= 50:
    print("ATCG")
    count += 2

print("My name is ", input("Enter your name: "))
print("My age is ", input("Enter your age: "))
print("My father name is ", input("Enter your father name: "))
print("My mother name is ", input("Enter your mother name: "))
print("My brother name is ", input("Enter your brother name: "))
print("My sister name is ", input("Enter your sister name: "))
print("My best friend name is ", input("Enter your best friend name: "))
print("My favourite food is ", input("Enter your favourite food: "))
print("My favourite drink is ", input("Enter your favourite drink: "))
print("My favourite colour is ", input("Enter your favourite colour: "))
print("My favourite sport is :", input("Enter your favourite sport: "))
print("My favourite subject is :", input("Enter your favourite subject: "))
print("My favourite subject is :", input("Enter your favourite subject: "))
print("My favourite subject is :", input("Enter your favourite subject: "))

x = input("Enter first number:")
y = input("Enter second number:")
print(int(x) + int(y))

name = "harryuuuuu"
friend = "rohan"
anotherfriend = "lovish"
apple = '''He said,'''
print("Hello," + name)
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

names = "Mubashir, Mubashir"
print(len(names))
fruits = "Mango", "apple", "banana"
print(len(fruits))
vegetables = "tomato", "potato", "onion"
print(len(vegetables))

vehicles = "car", "bike", "cycle"
print(len(vehicles))

a = "Mango"
print(a[0:4])

b = "banana"
print(b[0:4])

c = "apple"
print(c[0:4])

d = "tomato"
print(d[0:4])

f = "potato"
print(f[3:5])

g = "onion"
print(g[0:5])

h = "car"
print(h[0:3])

i = "bicycle"
print(i[0:3])

j = "monkey"
print(j[1:5])

a = "mubashir"
print(len(a))
print(a.upper())

b = "MUBASHIR"
print(len(b))
print(b.lower())

c = "arslaan"
print(len(c))
print(c.upper())

d = "ARSLAAN"
print(len(d))
print(d.lower())

e = "eshrat"
print(len(e))
print(e.upper())

f = "ESHRAT"
print(len(f))
print(f.lower())

g = "maisam"
print(len(g))
print(g.upper())

h = "MAISAIM"
print(len(h))
print(h.lower())

i = "atif"
print(len(i))
print(i.upper())

j = "ATIF"
print(len(j))
print(j.lower())

y = "!!!!mubashir!!!!!"
print(y.rstrip())

z = "!!!!!zahid!!!"
print(z.rstrip())

q = "!!!!!naina!!!!!"
print(q.rstrip())

w = "!!!wahab!!!!!!"
print(w.rstrip())

ahmira = "amrita"
print(ahmira.capitalize())

amrita = "ahmira"
print(amrita.replace("mubashir", "ahmed"))

a = "amrita"
print(a.count("amrita"))

b = "baloon"
print(b.count("baloon"))





      







