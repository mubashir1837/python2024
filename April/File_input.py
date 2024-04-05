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




