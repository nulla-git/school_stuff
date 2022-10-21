#Blake Reneau 10/19/22
#program that calculates the total area of some rooms given the amount of them and their dimensions,
#as well as account for rooms with abnormal corners.
i = 1
trianglesExist = input("are there abnormal corners of which can be represented by\na right triangle? (Y or N) ")

rooms = int(input ("how many rooms? "))
areas = []
def getRectangleArea(width, length):
    area = width * length
    return area

def getWeirdRoomArea(cornerLength, cornerWidth, cornerCount, width, length):
    cornerArea = (((cornerLength * cornerWidth)/2) * cornerCount)
    weirdArea = ((width * length) - cornerArea)
    return weirdArea


while rooms >= i and trianglesExist == "N":
    width = float(input ("width of room " + str(i) + " in meters? "))
    length = float(input ("length of room " + str(i) + " in meters? "))
    areas.append(getRectangleArea(width, length))
    i = i + 1
if rooms < i:
    print("the total area of the rooms is " + str(sum(areas)) + " square meters.")

while rooms >= i and trianglesExist == "Y":
    cornersExist = input("does this room have corners? (Y or N) ")
    width = float(input ("width of room " + str(i) + " in meters? "))
    length = float(input ("length of room " + str(i) + " in meters? "))
    if cornersExist == "N":
       areas.append(getRectangleArea(width, length))
       i = i + 1
       continue 
    elif cornersExist == "Y":
            cornerCount = int(input ("how many corners are there? "))
            cornerWidth = float(input ("width of a corner in meters: "))
            cornerLength = float(input ("length of a corner in meters: "))
            width = (width - cornerWidth)
            areas.append(getWeirdRoomArea(cornerLength, cornerWidth, cornercount)
            i = i + 1
            continue
    else:
        print("the total area of the rooms is " + str(sum(areas)) + " square meters.")
        break


