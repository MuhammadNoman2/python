# Assign string to a variable...
a = "Hello"
b = 'Hello'
print("Double Quotation ....    ", a)
print("Single Quotation..... ", b)
# Multiline String
c = """Hello Mr Hafi. 
How are you!. Whats's going on ..."""
print(c)
# Input...
# a = input("Enter Value to a : ")
# print(a)
# Indexes of String...
print(a, "starts with", a[0])
# String Properties.....
print(a, "Contains ", len(a), "Characters ...")
print(str.upper(a))
print(str.lower(a))
char = 'N'
print(ord(char))
print(chr(65))
# Check String ...
z = "I am not today .."
print("free " in z)
if "free" in z:
    print("free is present in ", z)
if "free" not in z:
    print("free is not present in ", z)
# Slicing Upper bound not include
b = "Hello, world!"
print(b[2:6])
print(b[:5])
print(b[6:])
# Removing White Space at Start
c = "   Hello, world!"
print(c.strip())
# Replace String

x = "My Name is Noman"
print(x)
print(x.replace("My Name is ", "Myself "))

a = "Hello"
b = "World!"
c = a + b
print(c)
c = a + " " + b
print(c)

# Format  string
age = 22
txt = "My name is Noman , and I am {}"
print(txt.format(age))

quality = 3
itemNo = 547
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollar."
result = myOrder.format(quality, itemNo, price)
print(result)
# print(myOrder.format(quality, itemNo, price))
# Escape Character
txt = "WE are so called \"Vikings\" from the \fNorth"
print(txt)
