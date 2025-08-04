info={
    'name':'Kartik',
    'age':18,
    'eligible':True
}
print(info.get("names"))#gives no error 


person = {
    "name":"Kartik",
    "age":18,
    "city":"Dehradun"
}

info.update(person)#this adds person dict key values to info 
# ep1.clear() to clear the dict

# #updating
# person["age"]=12
# print(person["age"])
# print(person["name"])
# # name is there
# # person.pop("name")
# # name is not there anymore 
# # print(person["name"])
# if "name" in person:
#     print("name exists")
# print(person.values())

# for key in person:
#     print(key)

# for values in person:
#     print(values)

  
