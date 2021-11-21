# Gage Hilyard

# Question 1

score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

wins = 0
losses = 0
for date, value in score_differences.items():
    if int(value) > 0:
        wins += 1
    else:
        losses += 1

print(wins, "wins -", losses, "losses")


#Question 2

class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    def __init__(self, manufacturer, coolant):
        Appliance.manufacturer = manufacturer
        self.coolant = coolant

    def __str__(self):
        return str("The " +self.manufacturer +" refrigerator contains refrigerant " +self.coolant)

    

my_refrigerator = Refrigerator("Samsung", "R134a")
print(my_refrigerator)
