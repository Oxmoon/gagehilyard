# --------------------------------------
# CSCI 127, Lab 6                      |
# February 21, 2019                    |
# Gage Hilyard                         |
# --------------------------------------

def average_magnitude(efile):
    total_magnitude = 0
    for i in range(1,len(efile)):
        total_magnitude += float(efile[i][9])
    average = (total_magnitude)/(len(efile))
    return average
# --------------------------------------

def earthquake_locations(efile):
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    name_list = []
    
    for i in range(1, len(efile)):
        if efile[i][12] not in name_list:
            name_list.append(efile[i][12])
        name_list.sort()
    for number in range(0,len(name_list)):
        print(str(number+1)+". " +name_list[number])

# --------------------------------------

def count_earthquakes(efile, lower_bound, upper_bound):
    count = 0
    for i in range(1, len(efile)):
        if float(efile[i][9]) >= lower_bound and float(efile[i][9]) <= upper_bound:
            count += 1
    return count

# --------------------------------------

def main(file_name):
# Converts CSV file to list
    import csv
    reader = csv.reader(open(file_name, 'r'))
    efile = list(reader)
# ------------------------------------------------------
    magnitude = average_magnitude(efile)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(efile)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(efile, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
