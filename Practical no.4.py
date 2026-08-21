# Program to perform operations on Tuple, Set and Dictionary

# -------- Tuple --------
t = (10, 20, 30, 40, 20)

print("Tuple:", t)
print("First element:", t[0])
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))


# -------- Set --------
s = {10, 20, 30, 40}

print("\nSet:", s)

s.add(50)
print("After adding 50:", s)

s.remove(20)
print("After removing 20:", s)

print("Union:", s.union({60, 70}))
print("Intersection:", s.intersection({30, 40, 50}))


# -------- Dictionary --------
student = {
    "name": "Ananya",
    "age": 18,
    "marks": 85
}

print("\nDictionary:", student)

print("Name:", student["name"])

student["city"] = "Nagpur"
print("After adding city:", student)

student["marks"] = 90
print("After updating marks:", student)

student.pop("age")
print("After removing age:", student)

print("Keys:", student.keys())
print("Values:", student.values())