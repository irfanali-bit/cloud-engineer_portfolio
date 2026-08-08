# ==========================================
# Chapter 5 : Loops
# File      : 06_break_continue.py
# Author    : Irfan Ali
# Topic     : break and continue
# ==========================================

for i in range(1, 11):
    if i == 5:
           break
    print(i)




print("----- CONTINUE -----")

for i in range(1, 6):
    if i == 3:
        continue

    print(i)