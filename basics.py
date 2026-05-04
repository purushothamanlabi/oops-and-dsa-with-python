
# Numeric Types
a = 10
b = 10.5
c = 2 + 3j
print("int:", a, type(a))
print("float:", b, type(b))
print("complex:", c, type(c))

# Boolean
d = True
print("bool:", d, type(d))

# String (Sequence)
e = "hello"
print("str:", e, type(e))

# List (Mutable Sequence)
f = [1, 2, 3]
print("list:", f, type(f))

# Tuple (Immutable Sequence)
g = (1, 2, 3)
print("tuple:", g, type(g))

# Set (Mutable)
i = {1, 2, 3}
print("set:", i, type(i))


# Dictionary (Mapping)
k = {"name": "abi", "age": 22}
print("dict:", k, type(k))


# Frozenset (Immutable)
j = frozenset([1, 2, 3])
print("frozenset:", j, type(j))


# Range
h = range(5)
print("range:", list(h), type(h))

# None Type
o = None
print("NoneType:", o, type(o))

name = 1
if name ==1:
    print("condition")
else:
    print("else condition ")

# Python has one for loop, but we use it with list, string, range, dictionary, tuple, set, etc.
for data in f:
    if data == 3:
        break
    print(data)
    if data ==2:
        continue
    
# switch 
match name :
    case 200:
        print()
    case 1:
        print()

# while True :
#     print("asas")

def function(here):
    try:
        return f"this is return:{here} "
    except Exception as e:
        print(e)
    finally:
        print("final")
    

print(function("abi"))

