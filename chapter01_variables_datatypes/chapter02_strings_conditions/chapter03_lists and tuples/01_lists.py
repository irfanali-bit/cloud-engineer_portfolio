# ==========================================
# Chapter 3 : Lists
# Topic : Introduction to Lists
# Author : Irfan Ali
# =========================================


#Examp 1

fruits = ["APPLE","BANANA","MANGO"]
print(fruits)

#Example 2

numbers = [10,20,30,40]
print(numbers)


#Example 3

students = ["irfan",22,True,75,5]
print(students)


#Example 4

languages = ["pyhon","java","C++","java"] 
print(languages)

# ==========================================
# Topic : Indexing
# ==========================================


#Exampl


fruits = ["APPLE","BANANA","MANGO"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# ==========================================
# Negative Indexing
# ==========================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])


# ==========================================
# slicing
# ==============

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0:2])
print(fruits[0:3])
print(fruits[1:3])
fruits[1] = "kivi"
print(fruits)
fruits[3] = "grapes"
print(fruits)