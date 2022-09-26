i = 0
#don't put a dot after input or int
desired_hours = int(input("how many hours do you wanna grow it for: "))
height = 100

while i < desired_hours:
    print("growing...")
    print(height)
    height = height * 1.5
    height += 30
    i += 1
