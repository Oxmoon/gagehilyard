# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Gage Hilyard                             |
# Last Modified: February 28, 2019         |
# -----------------------------------------+
#  |
# -----------------------------------------+
import csv

# -----------------------------------------+
# coldest_temperature                      |
# -----------------------------------------+
# Finds the Minimum temperature recorded   |
# in the file. Prints the temperature,     |
# the location where it was recorded and   |
# the date when it was recorded.           |
# -----------------------------------------+

def coldest_temperature(file_name):
    reader = csv.reader(open(file_name, 'r'))
    wfile = list(reader)
    minimum = int(wfile[1][7])
    for i in range(2, len(wfile)):
        if int(wfile[i][7]) < minimum:
            minimum = int(wfile[i][7])
            location = wfile[i][5]
            date = wfile[i][4]
    print("Coldest Fahrenheit temperature reading:" ,minimum)
    print("Location:", location)
    print("Date:", date)




# -----------------------------------------+
# average_temperature                      |
# -----------------------------------------+
# Gives average temperature of a given     |
# location.                                |
# -----------------------------------------+

def average_temperature(file_name, location):
    reader = csv.reader(open(file_name, 'r'))
    wfile = list(reader)
    count = 0
    total_temp = 0
    for i in range(1, len(wfile)):
        if (wfile[i][5]).lower() == location.lower():
            count += 1
            total_temp += int(wfile[i][0])
    average = (total_temp/count)
    print("Number of readings:",count)
    print("Average temperature: " +str("%.2f" % average))
    
            





# -----------------------------------------+
# all_stations_by_state                    |
# -----------------------------------------+
# Prints all stations by state             |
# -----------------------------------------+

def all_stations_by_state(file_name, state):
    reader = csv.reader(open(file_name, 'r'))
    wfile = list(reader)
    count = 0
    station_list = []
    for i in range(1, len(wfile)):
        if (wfile[i][11]).lower() == state.lower():
            if (wfile[i][5])[:-4] not in station_list:
                line = wfile[i][5]
                station_list.append(line[:-4])
                count += 1
                print(str(count) +". " +station_list[count-1])

# -----------------------------------------+
# average_rain                             |
# -----------------------------------------+
# prints average rainfall for 2016.        |
# -----------------------------------------+

def average_rain(file_name):
    reader = csv.reader(open(file_name, 'r'))
    wfile = list(reader)
    count = 0
    total_rain = 0
    for i in range(1, len(wfile)):
        if (wfile[i][13]) == "2016":
            count += 1
            total_rain += float(wfile[i][9])
    average = (total_rain/count)
    print("Number of readings in 2016:",count)
    print("Average weekly rainfall: " +str("%.2f" % average) +" inches")

# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Identify average weekly rainfall for 2016.")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            average_rain(input_file)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
