# ==========================================
# Chapter 4 : Set
# File      : 04_set_methods.py
# Author    : Irfan Ali
# Topic     : Set Methods
# ==========================================

print("===== SET METHODS =====")

numbers = {1, 2, 3, 4}

print("\n===== add()=====")
numbers.add(5)
print(numbers)

print("\n===== remove()=====")
numbers.remove(2)
print(numbers)

print("\n===== discard()=====")
numbers.discard(2)
print(numbers)

print("\n===== pop()=====")
numbers.pop()
print(numbers)

print("\n===== clear()=====")
numbers.clear()
print(numbers)

set1 = {1,2,3,}
set2 = {3,4,5}


print("\n===== union()=====")

print(set1.union(set2))


print("\n===== intersection()=====")
print(set1.intersection(set2))