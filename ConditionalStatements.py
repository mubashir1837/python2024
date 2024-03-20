str1 = "This is a string\t and we are using str in python"
str2 = "Mubashir.\n we are creating str it in python"
print(str2)
print(str1)

ali ="My name is Mubashir\n My father name is Muhammad Raza\n I study in class 12\n My age is 21"
print(ali)
a ="a\tb\tc\td\te\tf\tg\th\ti\tj\tk\tl\tm\tn\to\tp\tq\tr\ts\tt\tu\tv\tw\tx\ty\tz."
print(a)
abc = "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz"
print(abc)

int="1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
print(int)
inte = "1\t2\t3\t4\t5\t6\t7\t8\t9\t10"
print(inte)

### Concatenation
str1 = "Mubashir"
str2 = "Ali"
print(str1+str2)

a = "Apple "
b = "Ball"
print(a + b)

a = "23"
b = ("24")
final_str =a+b
print(final_str)

### Length of str

a = "ali"
print(len(a))
fbise ="Google,Facebook,Instagram"
print(len(fbise))


str3 = "MUBASHIR"
len2 = len(str3)
len3 = len2
print(len3)


a = "Apple"
b =len(a)
c = b
d = c
print(d)


#INDEXING
s ="Mubashir"
ch = s[3]
print(ch)

g = "google"
ch =g[4]
print(ch)

f = "Facebook"
ch = f[6]
print(ch)

w = "Whatsapp"
ch = w[3]
print(ch)

i = "Instagram"
ch = i[5]
print(ch)


### SLICING
str ="MUBASHIR"
print(str[1 : 4])

g = "GOOGLE"
print(g[0:4])
print(g[2:4])
print(g[3:4])


f = "FACEBOOK"
print(f[1:5])
print(f[0:4])
print(f[2:7])


c = "CHARACTERS"
print(c[1:5])
print(c[0:7])


i = "INSTAGRAM"
print(i[:])
print(i[0:])

# Negative Index
a = "APPLE"
print(a[-3:-1])
print(a[-5:-1])
print(a[-5:-2])


### STRING FUNCTIONS
#str.endswith("er")
#str.capitalize()
#str.replaced(old,new)
#str.find(word)
#str.count("am")

g = "Google is a source of information"
print(g.endswith("oogle"))
print(g.endswith("tion"))

f ="Facebook is a social media source"
print(f.endswith("source"))
print(f.endswith("gool"))

str = "i love my country"
print(str.capitalize())


g ="google"
print(g.capitalize())


f = "facebook"
print(f.capitalize())


i = "instagram"
print(i.capitalize())



g = "i am using google"
print(g.replace("e", "i"))


f ="I am using facebook"
print(f.replace("k", "f"))


i = "I am using Instagram"
print(i.replace("m","p"))


p = "I am using javascript"
print(p.replace("javascript","Python"))



g =" I  was using google"
print(g.find("using"))


f = " I was using Facebook"
print(f.find("WAS"))
print(f.find("was"))



i = "I was using using Instagram"
print(i.count("using"))

g =  "I am using google google"
print(g.count("google"))

str = "I am reading book"
print(str.count("o"))































