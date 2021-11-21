# -----------------------------------------
# Gage Hilyard, Joe Groth         
# CSCI 107, Assignment 9                   
# Last Updated: November 30, 2018            
# -----------------------------------------
# Use recursion to generate permutations.    
# -----------------------------------------

# -----------------------------------------
# permutations                             
# -----------------------------------------
# remaining: characters still to use       
# permutation: the permutation thus far    
# -----------------------------------------
# Generate and print each permutation      
# -----------------------------------------

def permutations(remaining, permutation_so_far = ""):
    if len(remaining) == 0:
        print(permutation_so_far)
    else:
        for ch in remaining:
            permutations(remaining.replace(ch, ""), (ch + permutation_so_far))

# -----------------------------------------
# process_text                             
# -----------------------------------------
# text: the text to process,               
#       no repeated characters             
# -----------------------------------------
# Print out the permutations of the text   
# in a readable format.
# -----------------------------------------

def print_permutations(text):
    print('Permutations of "' + text + '"')
    print("------------------" + ("-" * len(text)))
    permutations(text)
    print()

# -----------------------------------------
# main                                     
# -----------------------------------------
# This function has no parameters.         
# -----------------------------------------
# This function tests the functionality of 
# your solution on different inputs.       
# -----------------------------------------

def main():
    print_permutations("")
    print_permutations("a")
    print_permutations("ab")
    print_permutations("abc")
    print_permutations("1234")

# -----------------------------------------

main()
