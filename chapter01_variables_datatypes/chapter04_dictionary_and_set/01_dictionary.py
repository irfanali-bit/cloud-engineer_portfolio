# ==========================================
# Chapter 4 : Dictionary
# File      : 01_dictionary.py
# Author    : Irfan Ali
# Date      : 05-08-2026
# Topic     : Python Dictionary Basics
# ==========================================

student = {
"name": "irfan", 
"age": 22,
"goal": "cloud Engineering", 
"city": "losal",

}
print(student) 

print("\n===== ACCESSING VALUES =====")



print(student["name"])
print(student["age"])
print(student["goal"])
print(student["city"])


print("\n===== UPDATING VALUES =====")

student["age"] = 12
student["city"] = "mumbai"

print(student)


print("\n===== PROGRAM FINISHED =====")
