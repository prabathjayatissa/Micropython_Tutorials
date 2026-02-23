"""
🐍 MICRO PYTHON TUTORIAL (Single File)

Run this file and read along!
Everything is explained with comments.

Run:
    python micro_python_tutorial.py
"""

# ======================
# 1. PRINTING OUTPUT
# ======================

print("\n--- 1. Hello World ---")
print("Hello, world!")


# ======================
# 2. VARIABLES
# ======================

print("\n--- 2. Variables ---")

name = "Alex"     # string
age = 25          # integer
height = 1.75     # float
is_student = True # boolean

print(name, age, height, is_student)


# ======================
# 3. USER INPUT
# ======================

print("\n--- 3. Input ---")

user_name = input("Enter your name: ")
print("Nice to meet you,", user_name)


# ======================
# 4. CONDITIONS (IF/ELSE)
# ======================

print("\n--- 4. Conditions ---")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult ✅")
else:
    print("You are a minor 👶")


# ======================
# 5. LOOPS
# ======================

print("\n--- 5. Loops ---")

print("For loop:")
for i in range(5):
    print(i)

print("While loop:")
count = 0
while count < 3:
    print(count)
    count += 1


# ======================
# 6. FUNCTIONS
# ======================

print("\n--- 6. Functions ---")

def greet(name):
    return f"Hello {name}!"

print(greet("Sam"))


# ======================
# 7. LISTS
# ======================

print("\n--- 7. Lists ---")

fruits = ["apple", "banana", "orange"]
print(fruits[0])

fruits.append("grape")
print(fruits)


# ======================
# 8. DICTIONARIES
# ======================

print("\n--- 8. Dictionaries ---")

user = {
    "name": "Alex",
    "age": 25
}

print(user["name"])


# ======================
# 9. IMPORTING MODULES
# ======================

print("\n--- 9. Modules ---")

import math

print("Square root of 16:", math.sqrt(16))


# ======================
# 10. MINI CHALLENGE
# ======================

print("\n--- 10. Challenge ---")

name = input("Your name: ")
age = int(input("Your age: "))

if age >= 18:
    print(name, "can vote 🗳️")
else:
    print(name, "cannot vote yet")


print("\n🎉 Tutorial complete! You're officially started with Python.")

