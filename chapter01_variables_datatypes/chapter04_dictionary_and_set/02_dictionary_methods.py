# ==========================================
# Chapter 4 : Dictionary
# File      : 02_dictionary_methods.py
# Author    : Irfan Ali
# Date      : 05-08-2026
# Topic     : Dictionary Methods
# ==========================================

print("===== DICTIONARY METHODS =====")

#topic 1 : keys()

student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
print(student.keys())


#topic 2 : values()

print("\n===== values() METHOD =====")

student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
print(student.values())



#topic 2 : items()


student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
print(student.items())


#topic 4 : get


student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
print(student.get("name"))
print(student.get("phone"))

# topic 5 : update


student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
student.update({"age":12})
print(student)
student.update({"city":"bengluru"})
print(student)


# topic 6 :pop

student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
student.pop("age")
print(student)

 
# topic 7 :clear

student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}

student.clear()
print(student)

# topic 8 : len


student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}

print(len(student))