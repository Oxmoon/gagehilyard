import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# April 11, 2017                                  |
# Gage Hilyard                                    |
# -------------------------------------------------

def read_file(file_name):
    file = open(file_name, "r")
    school_file = file.readlines()
    name_array = np.array([])
    enrollment_array = np.array([])
    with open(file_name) as f:
        next(f)
        for line in f:
            values = line.split(",")
            name_array = np.append(name_array, values[0])
            enrollment_array = np.append(enrollment_array, int(values[1]))
    return name_array, enrollment_array
        

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)

    plt.figure("Montana State University Fall 2018 Enrollments")
    plt.ylabel("College Enrollment")
    plt.xlabel("College Name")

    positions = [0, 1, 2, 3, 4, 5, 6]

    plt.bar(positions, college_enrollments, width=0.5, color=("blue","yellow"))
    y_pos = np.arange(0, 4401, 400)
    plt.yticks(y_pos)
    plt.xticks(positions, college_names)
    
    plt.show()

# -------------------------------------------------

main("fall-2018.csv")
