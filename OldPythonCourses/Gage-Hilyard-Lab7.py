# --------------------------------------
# CSCI 127, Lab 7                      |
# February 28, 2019                    |
# Gage Hilyard                         |
# --------------------------------------

def create_dictionary(file_name):
    code_file = open(file_name, "r")
    code_dict = {}
    for line in code_file:
        (numbers, value) = line.split(',')
        if value[:-1]== 'space':
            code_dict[" "] = numbers
        elif value[:-1] == 'comma':
            code_dict[","] = numbers
        else:
            code_dict[value[:-1]] = numbers
    code_file.close()
    return code_dict

# --------------------------------------

def translate(sentence, dictionary, output_file_name):
    output_file = open(output_file_name, "w")
    for ch in sentence:
        if ch in dictionary:
            output_file.write(ch +" " +dictionary[ch]+"\n")
        else:
            output_file.write(ch +" " +"UNKNOWN\n")
    print()
# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()
