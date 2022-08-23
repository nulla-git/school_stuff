newline_hello = """Hello,
World!"""
fox = " A Lazy Fox sleeps under a Tree."
hello = "Hello, World!"
x = "Tree" in fox
y = "Lazy" not in fox
a = "Red"
b = "Apple"
apple = "The apple is "
apple_format = "The apple is {}"

print("Hello")
print('Hello')

print("-----------")




print(newline_hello)
print(hello[4])
print(hello[6:12])
print(hello[-11:-7])
print("-----------")
print(len(hello))
print(fox.strip())
print(fox.lower())
print(fox.upper())
print(fox.replace("Fox", "Pig"))
print(hello.split(","))
print("-----------")
print(x)
print(y)
print(a + b)
print(a + " " + b)

print(apple + a)
print(apple_format.format(a))