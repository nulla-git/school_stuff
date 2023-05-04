# Blake Reneau 04/04/23
# draw a line
import time

offset = 0
while offset <= 11:
    time.sleep(0.25)
    print((" " * offset) + "0")
    offset += 1

while offset >= 1:
    time.sleep(0.25)
    offset = offset - 1
    print((" " * offset) + "0")
