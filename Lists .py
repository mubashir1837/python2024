### LISTS IN PYTHON:
marks1 = 74.5
marks2 = 70.9
marks3 = 68.1
marks4 = 65.4
marks5 = 63.7
marks = [74.5, 70.9,68.1,65.4,63.7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(len(marks))

student = ["Mubashir",19,95.5,"FBISE"]
print(student[0])
student[0] = "Ali"
print(student)
## Slicing
print(student[ : 2])
print(student[1 : 3])



list =[2,3,4,5]
list.append(6)
print(list)
list.append(8)
print(list)
list.append(988)
print(list)



alpha = [3,2,6,5,4,1,0]
print(alpha.sort())
print(alpha)


beta = [9,8,5,6,7,4,3,2,1]
print(beta.sort())
print(beta)


gamma = [6,5,7,3,2,1,0,4,5,9,8]
print(gamma.sort(reverse= True))
print(gamma)

abc =["Ball","Apple","Dog","Car" ]
print(abc.sort())
print(abc)


letters = ["a","b","c","e","f"]
print(letters.sort(reverse= True))
print(letters)

letter = ["d","e","c","d","b","a"]
print(letter.sort())
print(letter)


hydro = [1,2,3,4,5,6,7,8,9]
hydro.reverse()
print(hydro)


abc = [1, 3, 9, 5]
abc.insert(2 , 5)
print(abc)

### LIST METHOD
## list.append(4)
Google =[1, 2 ,3,4]
print(Google.append(4))
print(Google)
print(Google.append(67))
print(Google)
print(Google.append(5))
print(Google)
print(Google.append(32))
print(Google)
print(Google.append(455))
print(Google)
print(Google.append(90))
print(Google)
print(Google.append(1))
print(Google)
print(Google.append(2))
print(Google)
print(Google.append(3))
print(Google)
print(Google.append(4))
print(Google)

## list.sort() ascending order
facebook =[4,3,2,6,5,1,9,8,7]
print(facebook.sort())
print(facebook)

google = ["a","e","b","c","f","d","h","g"]
print (google.sort())
print(google)
## list.sort(reverse = True)Descending order
facebook =[1,2,3,4,5,6,7,8,9]
print(facebook.sort(reverse = True))
print(facebook)

instagram =[4,3,2,1]
print(instagram.sort(reverse = True))
print(instagram)
# .....case
facebook = [9,8,7,4,33]
print(facebook.sort())
print(facebook)

## list.reverse()
google = [5,4,3,2,1]
print(google.reverse())
print(google)


##list.inser(ind, el)
google = [1,2,3,4,5,6]
google.insert(4 , 99)
print(google)

facebook =[3,5,4,6,1,2,8]
facebook.insert(3, 313)
print(facebook)

instagram = [1,5,3,5,8,6,4,6]
instagram.insert(5 , 7778888)
print(instagram)

##list.remove(1)
list =[2,1,3,1]
list.remove(3)
print(list)

google = [6,5,4,3,2,8,7,4]
google.remove(6)
print(google)

facebook = [4,5,77,6]
facebook.remove(77)
print(facebook)

instagram = [4,3,26,54,22]
instagram.remove(26)
print(instagram)


### list.pop(idx)
list = [3,4,5,6]
list.pop(2)
print(list)

google = [5,4,3,67,5,65]
google.pop(5)
print(google)

facebook = [5,3,2,6,8,7,9]
facebook.pop(2)
print(facebook)

instagram =[67,78,877,988,88]
instagram.pop(3)
print(instagram)


