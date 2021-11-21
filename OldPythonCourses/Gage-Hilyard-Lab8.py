# -----------------------------------------------------
# CSCI 127, Lab 8
# March 7, 2019
# Gage Hilyard
# -----------------------------------------------------

class Contact:
    
    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.number = number
        self.title = ""

    def print_entry(self):
        if self.title == "":
            print(self.first +" " +self.last +self.number.rjust((25 +len(self.number)) - (len(self.first)+1+len(self.last))))
        else:
            print(self.title +" " +self.first +" " +self.last \
                  +self.number.rjust((25 +len(self.number)) - (len(self.title)+1+len(self.first)+1+len(self.last))))

    def set_first_name(self, new_first_name):
        self.first = new_first_name

    def set_title(self, title):
        self.title = title

    def get_cell_number(self):
        return self.number

    def get_area_code(self):
        return self.number[:3]

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
