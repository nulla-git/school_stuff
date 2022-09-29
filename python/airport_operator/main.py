#Blake Reneau 9/29/22
#simple airport operator simulator

requests = 0
#maximum capacity needs to be 3
capacity = 0

print("luton airport is open")

while requests < 5:
    requests += 1
    print("please state condition and intentions.")
    weather = input("what is the weather? (sunny, cloudy, or rainy): ")
    windSpeed = int(input("what is the windspeed in MPH? "))
    intent = input("do you want to land or takeoff? ")
    takeoff_allowed = ((weather == "sunny" and windSpeed <= 30) or
        (weather == "cloudy" and windSpeed <= 20) or 
        (weather == "rainy" and windSpeed <= 10))
    landing_allowed = ((weather == "sunny" and windSpeed <= 25) or
        (weather == "cloudy" and windSpeed <= 15) or 
        (weather == "rainy" and windSpeed <= 5))
    if intent == "land" and landing_allowed == True:
        capacity += 1
        print("free to land.")
        continue
    elif landing_allowed == False or capacity == 3:
        print("the conditions here are unsafe to land, find somewhere else.")
        continue
    if intent == "takeoff" and takeoff_allowed == True:
        print("clear for takeoff")
        if capacity > 0:
            capacity -=1
        continue
    elif takeoff_allowed == False:
        print("please wait, as it is unsafe to takeoff as of now.")
        continue

print("luton airport is now closed, please never come again.")
