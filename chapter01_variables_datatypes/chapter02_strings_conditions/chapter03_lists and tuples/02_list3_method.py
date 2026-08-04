# ====================================
# Chapter 3 : Lists
# Topic : List Methods
# Author : Irfan Ali
# ====================================

fruits = ["apple","banana"]
print(fruits)
fruits.append("mango")
print(fruits)

#example 2 : insert()

fruits = ["apple","banana","mango"]
fruits.insert(1,"orange")
print(fruits)

#example 3 : remove

fruits = ["apple","banana","mango"]
fruits.remove("banana")
print(fruits)

#example 4 :pop

fruits = ["apple","banana","mango"]
fruits.pop(0)

#example 5 : sort

fruits = ["banana","mango","apple", "blueberry", "pear","kivi"]
fruits.sort()
print(fruits)


fruits = ["banana","mango", "pear","apple","kivi", "blueberry"]
fruits.sort(reverse=True)
print(fruits)



#example 5 : reverse

fruits = ["banana","mango","apple", "blueberry"]
fruits.reverse()
print(fruits)

fruits = ["banana","mango","apple", "blueberry"]
fruits.clear()
print(fruits)
