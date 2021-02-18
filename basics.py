# Eimar Michelle Quinn
# Python Basics
# 17/02/2021

# println
print("Hello, World!")

#a = 1 # int
#b = 1.0 # float
#s = "Hello, World from a string!" # string
#t = 'Hello, from a different string' # string

#print(a, b, s, t)

# print(s[:2.])

x = [1, 2, 3]
#print(x)
#print(x[0])
#print(x[2])
#print(x[-1])

# for loop
#for i in x:
#    print(i)
#    print (i +i)

# for loop, syntax asking for every second element
#for i in x[::2]:
#    print(i)
#    print(i + i)

# loop through integers, list view
#for i in range(10):
#    print(i)

# dictionary
d = {"no_wheels": 4, "make": "Skoda"}
print(d["no_wheels"])

d["model"] = "Superb"

print(d["model"])

# list comprehension
r = [1, 2, 3, 4]
print(r)

s = [i*i for i in r]
print(s)