f = open("demo.txt", "r") #read file
data = f.read(5)
print(data)
print(type(data))

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()

f =open("demo.txt", "w") #write file

f.write("I want to learn JavaScipt tomorrow. 123")

f.close()

f = open("demo.txt", "a") #append
f.write("Then I")

f = open("demo.txt", "r+")
f.write("abc")
f.close()


#with Syntax

import os
os.remove("demo.txt")

with open("practice.txt","w") as f:
    f.write("Hi every\n am learning file")
    f.write("Using Python\n I love programming")


with open("practice.txt", "r") as f:
    data =f.read()

new_data = data.replace("Python", "Java")
print(new_data)

word = "love"
with open("practice.txt","r") as f:
    data =f.read()
    if(data.find(word)) != -1:
        print("Found")
    else:
        print("not found")


