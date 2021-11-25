import json
import urllib.parse
import requests
import climage  
from colored import fg, bg, attr

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QzJEMxpGCINF81iU0qaANwNZesHMhO8x"

while True:
    orig = input("%sStarting Location: %s" % (fg(11), attr(0)))
    if orig == "quit" or orig == "q":
        break    
    dest = input("%sDestination: %s" % (fg(11), attr(0)))
    if dest == "quit" or dest == "q":
        break    

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    # additional variables
    system = input("%sMetric or Imperial System?: %s" % (fg(11), attr(0)))
    fuelAsk = input("%sWould you like to compute the how much the used fuel will cost? [y/n] %s" % (fg(11), attr(0)))

    if json_status == 0:
        print("%sAPI Status: %s " % (fg(45), attr(0)) + str(json_status) + " = A successful route call. \n")
        color = fg('turquoise_2') + attr('reset')

        if json_status == 0 :
            if system == "metric" or system == "m":     # choose metric system
                print("%sAPI Status: %s" % (fg(45), attr(0)) + str(json_status) + " = A successful route call. \n")
                print("=============================================")
                print("%sDirections from %s" % (fg(45), attr(0)) + (orig) + " to " + (dest))
                print("%sTrip Duration:   %s" % (fg(45), attr(0)) + (json_data["route"]["formattedTime"]))
                print("%sKilometers:      %s" % (fg(45), attr(0)) + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
                print("%sFuel Used (Ltr): %s" % (fg(45), attr(0)) + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
                print("=============================================")

                # fuel computation
                if fuelAsk == "y":
                    fuelPrice = input("%sPlease input the price of your fuel: %s" % (fg(45), attr(0)) )
                    fuelPrice = float(fuelPrice)
                    print("%sTotal Fuel Cost: %s" % (fg(45), attr(0)) + str("{:.2f}".format((fuelPrice * (json_data["route"]["fuelUsed"])*3.78))))
                    print("=============================================")
                elif fuelAsk == "n":
                    print("\n")
                    
                for each in json_data["route"]["legs"][0]["maneuvers"]:
                    print ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + "km)"))
                print("=============================================\n")

                output = climage.convert("map.png")
                print(output)
                
            elif system == "imperial" or system == "i":   # choose imperial system
                print("%sAPI Status: %s" % (fg(45), attr(0)) + str(json_status) + " = A successful route call. \n")
                print("=============================================")
                print("%sDirections from %s" % (fg(45), attr(0)) + (orig) + " to " + (dest))
                print("%sTrip Duration:   %s" % (fg(45), attr(0)) + (json_data["route"]["formattedTime"]))
                print("%sMiles:           %s" % (fg(45), attr(0)) + str(json_data["route"]["distance"]))
                print("%sFuel Used (Gal): %s" % (fg(45), attr(0)) + str(json_data["route"]["fuelUsed"]))
                print("=============================================")

                # fuel computation
                if fuelAsk == "y":
                    fuelPrice = input("%sPlease input the price of your fuel: %s" % (fg(45), attr(0)) )
                    fuelPrice = float(fuelPrice)
                    print("%sTotal Fuel Cost: %s" % (fg(45), attr(0)) + str("{:.2f}".format((fuelPrice * (json_data["route"]["fuelUsed"])))))
                    print("=============================================")
                elif fuelAsk == "n":
                    print("\n")

                for each in json_data["route"]["legs"][0]["maneuvers"]:
                    print ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + "km)"))
                print("=============================================\n")

                output = climage.convert("map.png")
                print(output)

    elif json_status == 402:
        print("*********************************************")
        print("%sStatus Code: %s" % (fg(1), attr(0))  + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("*********************************************\n")
    elif json_status == 611:
        print("*********************************************")
        print("%sStatus Code: %s" % (fg(1), attr(0)) + str(json_status) + "; Missing an entry for one or both locations.")
        print("*********************************************\n")
    else:
        print("**********************************************************************")
        print("%sFor Status Code: %s" % (fg(1), attr(0)) + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("**********************************************************************\n")