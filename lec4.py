"""
Lecture 4 tuple and dictionary
"""

my_tuple = "a","b","c","d","e"


#slice. first index is inclusive, second is exclusive
#tuple. with one value = ("a",)


#print(my_tuple[])

#my_2nd_tuple = ("a","b","c","d","e")
#print(my_2nd_tuple)

#test = "a",

#print(type(test))

#Dictionary 

my_car = {
        "color":"red",
        "maker":"toyota",
        "year":"2015"
           }
#print(my_car.items())

#print(my_car.keys())

#print(my_car.values())

#print(my_car.get("year"))

my_car["model"] = "corolla"


my_car["year"] = "2020"

print(my_car)

print(len(my_car))

print("color" in my_car)