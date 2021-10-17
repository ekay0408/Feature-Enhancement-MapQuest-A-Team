import json
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "G6YCn5dNaSGvufdGp63IFq45Gvr8J8bC"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break    
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break    

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    # additional variables
    system = input("Metric or Imperial System?: ")
    fuelAsk = input("Would you like to compute the how much the used fuel will cost? [y/n] ")

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call. \n")

        if json_status == 0 :
            if system == "metric" or system == "m":     # choose metric system
                print("API Status: " + str(json_status) + " = A successful route call. \n")
                print("=============================================")
                print("Directions from " + (orig) + " to " + (dest))
                print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
                print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
                print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
                print("=============================================")

                # fuel computation
                if fuelAsk == "y":
                    fuelPrice = float(input("Please input the price of your fuel: "))
                    print("Total Fuel Cost: " + str("{:.2f}".format((fuelPrice * (json_data["route"]["fuelUsed"])*3.78))))
                    print("=============================================")
                elif fuelAsk == "n":
                    print("\n")
                    
                for each in json_data["route"]["legs"][0]["maneuvers"]:
                    print ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + "km)"))
                print("=============================================\n")
                
            elif system == "imperial" or system == "i":   # choose imperial system
                print("API Status: " + str(json_status) + " = A successful route call. \n")
                print("=============================================")
                print("Directions from " + (orig) + " to " + (dest))
                print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
                print("Miles:           " + str(json_data["route"]["distance"]))
                print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
                print("=============================================")

                # fuel computation
                if fuelAsk == "y":
                    fuelPrice = float(input("Please input the price of your fuel: "))
                    print("Total Fuel Cost: " + str("{:.2f}".format((fuelPrice * (json_data["route"]["fuelUsed"])))))
                    print("=============================================")
                elif fuelAsk == "n":
                    print("\n")

                for each in json_data["route"]["legs"][0]["maneuvers"]:
                    print ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + "km)"))
                print("=============================================\n")

    elif json_status == 402:
        print("*********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("*********************************************\n")
    elif json_status == 611:
        print("*********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("*********************************************\n")
    else:
        print("**********************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("**********************************************************************\n")
