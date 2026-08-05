student = {

"name": "irfan",
"age": 22,
"city" : "losal",
"goal" : "cloud computing",

}

print(type(student))
print(student["goal"])
student["city"] = "jaipur"
print(student)

book_info= {
"book": "python",
"pages": 500,
"price": 999,
}
print(dict.keys())
print(dict.values())
print(dict.items())

dict.update({"sales":21})
print(dict)
print(len(dict))