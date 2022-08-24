newline_hello = """Hello,
World!"""
fox = " A Lazy Fox sleeps under a Tree."
hello = "Hello, World!"
x = "Tree" in fox
y = "Lazy" not in fox
amount = 7
color = "Red"
fruit = "Apple"
apple = "The apple is "
apple_format = "The apple is {}"
order = "I would like {} {} {}s, please."
order_ordering = "Are you sure that {2} number {0} is {1}?"

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
print(color + fruit)
print(color + " " + fruit)

print(apple + color)
print(apple_format.format(color))

print(order.format(amount, color, fruit))
print(order_ordering.format(amount, color, fruit))

print("-----------")

input_name = input("Enter your name: ")

print("Hello, " + input_name)

print("-----------")

pla = input("input value: ")
print(pla)

print("-----------")

foo = input("your name: ")
print("hi " + foo + ".")
bar = input("age: ")
print("you're " + str(bar) + "? that's pretty cool " + foo + ".")