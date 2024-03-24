information ={
    "Name" : "Mubashir",      ## "name"(key) : "Ali"(value)
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
print(result["ALI"]) ###  to find 32.



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



food = {
    "street1" : "10 ton",
    "street2" : "5 ton",
    "street3" : "2.3 ton"
}
print(food)
print(type(food))
print(len(list(food.values())))

laguages ={
    "passenger1" : "suit case",
    "passenger2" : "Box",
    "passenger3" : "Bag"
}
print(len(list(laguages.values())))

print(laguages.keys)


property ={
    "1kanal" :"25 lac",
    "2kanal" : "50 lac",
    "3kanal" : "75 lac"
}
print(len(list(property.keys())))

print(property.keys())

### .items()

water ={
    "5litres" : "500Rs",
    "4litres" : "400Rs",
    "3litres" : "300Rs",
    "2litres" : "200Rs",
    "1litres" : "100Rs"
}
print(water.items())


### .get("key")
mobile ={
    "oppo" : "25000",
    "techno" : "50000",
    "huawei" : "70000",
    "iphone" : "100000"
}
print(mobile.get("techno"))
print(type(mobile)) ## <class dict>
print(mobile["oppo"])
print(mobile.get("iphone"))
print(mobile["huawei"])


### .update(new dict)

letters ={
    "A" : "Apple",
    "B" : "Ball",
    "C" : "Cat"
}
letters.update({"D" : "Doll"})
print(letters)



social = {
    "g" : "Google",
    "f" : "Facebook",
    "i" : "instagram",
    "y" : "youtube"
}
social.update({"l" : "linkedin"})
print(social)




socials = {
    "s" : "Snapchat",
    "w" : "whatsapp",
    "x" : "Twitter",
    "c" : "chrome"
}
new_dict = {"s" : "skype"}
socials.update(new_dict)
print(socials)




items = {
    "B" : "Bottle",
    "A" : "Aeroplane",
    "L" : "Lion", ##duplicate keys not allowed
    "L" : "Leopard"
}
add_items ={"S" : "Sparrow"}
items.update(add_items)
print(items)




results_of_students = {
    "Ali" : 1047,
    "Ahmed" : 900,
    "Arsalan" : 880,
    "Aqib" : 700
}
results_of_students.update({"Adil" : "1000"})
print(results_of_students)




numbers = {
    "Touqeer" : 500,
    "Rahat" : 600,
    "Rashid" : 450,
    "Shumail" : 730
}

### .update (new dict)
add_student ={"Asif" : "30"}
numbers.update(add_student)
print(numbers)

#or
numbers.update({"Amjad" : "400"})
print(numbers)

numbers.update({"Alia" : "498"})
print(numbers)

numbers.update({"Maisam" : "454"})
print(numbers)

numbers.update({"Aneela" : "390"})
print(numbers)


print(numbers.update({ "Sara" : "300"}))
print(numbers)


print(numbers.update({"Nimra" : "568"}))
print(numbers)


print(numbers.update({"Khalid" : "1100"}))
print(numbers)

### .get("key")
print(numbers.get("Khalid"))
print(numbers.get("Rahat"))
print(numbers.get("Aneela"))
print(numbers.get("Sara"))
print(numbers.get("Maisam"))
print(numbers.get("Amjad"))
print(numbers.get("Alia"))
print(numbers.get("Nimra"))
print(numbers.get("Shumail"))


###.items()
print(numbers.items())


### To change the value
numbers["Rahat"] = "1300"
print(numbers)
numbers["Shumail"] = "900"
print(numbers)
numbers["Touqeer"] = "1330"
print(numbers)
numbers["Rashid"] = "1240"
print(numbers)
numbers["Khalid"] = "1310"
print(numbers)