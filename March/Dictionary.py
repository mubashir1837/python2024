information ={
    "key" : "Mubashir",
    "name" :"Ali",
    "learning" : "coding"
}
print(information)


google = {
    "facebook" : "chrome",
    "insta" : "messenger",
    "whatapp" : "status",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
}
print(google)

students = {
    "sec1" : 32,
    "sec2" : 39,
    "sec3" : 41,
    "sec4" : 45,
}
print(type(students)) ## <class dic>
print(students)


result ={
    "ALI" : 32,
    "AHMED" : 38,
    "QASIM" : 45,
    "AMJAD" : 50,
}
print(type(result)) ## <class dic>
print(result)
print(result["ALI"]) ### 32 to find.



prices = {
    "laptop" : 30000,
    "computer" : 20000,
    "TV" : 400000
}
prices["laptop"] = "60000" #change value in "laptop"
print(prices)
print(type(prices))
print(prices["TV"])

## Null dic
null_dic ={}
print(null_dic)


empty = {}
print(empty)

##Nested Dictionary
students ={
    "name" : "Mubashir",
    "subjects" : {
        "chem" : 80,
        "phy" : 90,
        "bio" : 79,
        "Eng" : 50
    }
}
print(students)
print(students["subjects"])


## Dictionary Method
#1).keys()

print(students.keys())
print(len(students))
## OR
print(len(list(students.keys())))


## .values()
print(students.values())
print(list(students.values()))



