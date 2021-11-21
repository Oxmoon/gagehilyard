import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# ------------------------------------------------+
# CSCI 127, Lab 13                                |
# April 18, 2019                                  |
# Gage Hilyard                                    |
# ------------------------------------------------+

def main(file_name):
    # read the file_name into a pandas dataframe
    data = pd.read_csv(file_name)
    
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"
    a = list(data.columns)
    x_axis = a[0]
    y_axis = a[1]
    data.plot(title=file_name[:-4], legend=None, x=x_axis, y=y_axis, kind="bar", color=("blue","yellow"))
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
