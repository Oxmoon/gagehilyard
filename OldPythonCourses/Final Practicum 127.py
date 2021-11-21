# Final Practicum CSCI 127
# Question One

##def while_loop_solution(word):
##    answer = ""
##    while word != "":
##        answer += word[0]
##        word = word[3:]
##    return answer
##
##
##def recursion_solution(word):
##    if word == "":
##        return ""
##    elif word[0] != "":
##        return word[0] + recursion_solution(word[3:])
##    else:
##        return recursion_solution(word[3:])
##
##
##word = "abcdefghijklmnopqrstuvwxyz"
##result = while_loop_solution(word)
##print(result)
##result = recursion_solution(word)
##print(result)

# Question Two

##import numpy as np
##
##def sum_border(matrix):
##    rows, columns = matrix.shape
##    rows = rows-1
##    columns = columns-1
##    total = 0
##    for x in range(0, rows+1):
##        for y in range(0, columns+1):
##            if x == 0 or x == rows:
##                total += matrix[x][y]
##            if y == 0 and x != 0 and x != rows:
##                total += matrix[x][y]
##            if y == columns and x != 0 and x != rows:
##                total += matrix[x][y]
##    return total
##    
##rows = int(input("Enter number of rows [1-10]: "))
##columns = int(input("Enter number of columns [1-10]: "))
##matrix = np.random.randint(1, 11, rows*columns).reshape(rows,columns)
##print("Matrix Shape:", matrix.shape, " Matrix:\n", matrix)
##result = sum_border(matrix)
##print("The sum of the numbers on the four borders =", result)

# Question Three

##import matplotlib.pyplot as plt
##import numpy as np
##
##
##year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
##rainfall = np.random.randint(5, 20, 10)
##y_pos = np.arange(len(year))
##
##plt.barh(y_pos, rainfall, align='center')
##plt.yticks(y_pos, year)
##plt.ylabel("Year")
##plt.xlabel('Rainfall')
##plt.title('Precipitation Horizontal Bar Graph')
##
##plt.show()

# Question Four

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("publishers.csv")

genre_sales = data.groupby("genre")["sale price"].sum()
genre_graph = genre_sales.plot(title="Amazon Book Sales",\
                               kind="bar")
plt.show()
