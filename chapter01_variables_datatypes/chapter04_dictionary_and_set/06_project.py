# ==========================================
# Chapter 4 : Dictionary & Set
# File      : 06_project.py
# Author    : Irfan Ali
# Topic     : Student Database Project
# ==========================================

print("===== STUDENT DATABASE PROJECT =====")

student = {
    "name": "Irfan",
    "age": 22,
    "goal": "Cloud Engineer",
    "city": "Losal"
}

skills = {
    "Python",
    "Linux",
    "Git",
    "GitHub",
    "Python"     # Duplicate
}

print("\n===== STUDENT DETAILS =====")

print("Name    :", student["name"])
print("Age     :", student["age"])
print("Goal    :", student["goal"])
print("City    :", student["city"])

print("\n===== UPDATE CITY =====")

student["city"] = "Sikar"

print(student)

print("\n===== SKILLS =====")

print(skills)

print("\n===== TOTAL SKILLS =====")

print(len(skills))

print("\n===== ADD NEW SKILL =====")

skills.add("AWS")

print(skills)

print("\n===== PROGRAM FINISHED =====")