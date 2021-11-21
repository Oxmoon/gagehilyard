# Practicum 2
# Question One

##word_count = {"apple": 10, "banana": 15, "coconut": 6}
##for (key, value) in word_count.items():
##    print(key, value)

# Question Two

##class Movie():
##    def __init__(self, title, director):
##        self.title = title
##        self.director = director
##
##    def __str__(self):
##        return str('The movie ' +'"' +self.title +'" was directed by ' +self.director)
##        
##movie_1 = Movie("Bao", "Domee Shi")
##print(movie_1)
##movie_2 = Movie("Between the Lines", "Maria Koneva")
##print(movie_2)

# Question Three

def retain_every_other_line(input_file_name, output_file_name):
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")
    count = 1
    for line in input_file:
        if count % 2 == 1:
            output_file.write(line)
        count += 1
    input_file.close()
    output_file.close()

retain_every_other_line("Practicum2_input_file.txt", "Practicum2_output_file.txt")
