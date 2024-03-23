### Tuples
tup =(2,2,3,4,5,1)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(type(tup))

##slicing
tup =(1,3,5,2,3)
print(tup.index(2))
print(tup.count(2))


### WAP to ask the user to enter names of their3 favourite movies and store them in a list.
movies =[]
mov1 = input("enter 1st movie")
movies.append(mov1)
mov2 = input("enter second movie")
movies.append(mov2)
mov3 = input("input third movie")
movies.append(mov3)

print(movies)

google = []
google.append(input("facebook1"))
google.append(input("facebook2"))
google.append(input("facebook3"))

print(google)

tup = []
tup.append(input("value1 :"))
tup.append(input("value2 :"))
tup.append(input("value3 :"))
tup.append(input("value4 :"))

print(tup)



### Palindrome: same head and tail.
#for example: "maam" [1,2,3,2,1] "racecar"

list1 = [1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

list2 =["A","B","C","C","B","A"]
copy_list2 = list2.copy()
copy_list2.reverse
if (copy_list2 == list2):
    print("Palindromic")
else:
    print("Not Palindromic")


### WAP to count the number of student with the "A" grade inthe following tuple.
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))
print(grade.count("B"))

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)


