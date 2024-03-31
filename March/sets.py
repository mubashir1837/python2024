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




