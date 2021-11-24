import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "7PoLIYVHFdnu6VC5ZCpwxL9Avrg6h0vV"

while True:
    username = input("Please Input Your Name: ")
    if username == "quit" or username == "q":
        break
    print("Car, Airplane, Boat, Busses, or Train.")
    vehicle = input("Please Input Type of Transportation: ")
    if vehicle == "quit" or vehicle == "q":
        break
    persons = input("How many passengers: ")
    if persons == "quit" or persons == "q":
        break
    personsInt = int(persons)
    if (vehicle.lower() == "car" or vehicle.lower() == "airplane" or vehicle.lower() == "boat" or vehicle.lower() == "busses" or vehicle.lower() == "train"):
        orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            break
        dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            break
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            if (vehicle == "car"):
                print("The Toll Fee is $10")
            elif (vehicle == "airplane"):
                print("The Toll Fee is $12")
            else:
                print("No Toll Fee")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration: " + (json_data["route"]["formattedTime"]))
            print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
            print("=============================================")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
            print("Name: " + username)
            print("Vehicle Type: " + vehicle.lower())
            print("Number of Passengers: " + str(personsInt))
            if (vehicle.lower() == "car"):
                print("Your Total Fee is : " + str("{:.2f}".format((personsInt)*(10)+(50)*(json_data["route"]["distance"])*1.61)))
            elif (vehicle.lower() == "airplane"):
                print("Your Total Fee is : " + str("{:.2f}".format((personsInt)*(200)*(json_data["route"]["distance"])*1.61)))
            elif (vehicle.lower() == "boat"):
                print("Your Total Fee is : " + str("{:.2f}".format((personsInt)*(150)*(json_data["route"]["distance"])*1.61)))
            elif (vehicle.lower() == "busses"):
                print("Your Total Fee is : " + str("{:.2f}".format((personsInt)*(12)+(30)*(json_data["route"]["distance"])*1.61)))
            elif (vehicle.lower() == "train"):
                print("Your Total Fee is : " + str("{:.2f}".format((personsInt)*(70)*(json_data["route"]["distance"])*1.61)))
            print("=============================================\n")

        elif json_status == 402:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("For Staus Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")
    else:
        print("Please choose a correct Vehicle!")