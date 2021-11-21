import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# ------------------------------------------------+
# CSCI 127, Program 6                             |
# April 25, 2019                                  |
# Gage Hilyard                                    |
# ------------------------------------------------+

# -------------------------------------------------

def main(file_name):

    data = pd.read_csv(file_name)

    # Average Security delays by Airport per Month
    security_average = data.groupby("Code")["# of Delays.Security"].mean()
    security_graph = security_average.plot(title="Average Security Delays Per Month",\
                                           kind="bar", color=("blue","green"))
    security_graph.set(xlabel="Airport", ylabel="Avg. # of Delays")
    plt.show()

    # Average Weather delays by Month In the US by Minutes
    monthly_delay = data.groupby("Month Name")["Minutes Delayed.Weather"].mean()
    monthly_graph = monthly_delay.plot(title="Average Weather Delay by Month Across the US",\
                                       kind="line", color=("turquoise","pink"))
    monthly_graph.set(xlabel="Month", ylabel="Average Minutes")
    plt.show()

    

# -------------------------------------------------

main("airlines.csv")
