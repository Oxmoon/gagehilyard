# -----------------------------------------
# Gage Hilyard                                
# CSCI 107, Assignment 4                   
# Last Updated: October 3, 2018                   
# -----------------------------------------
# Use loops to minimize repeated words and 
# phrases to these lyrics of "The Fox".   
# -----------------------------------------

hook = str("WHAT DOES THE FOX SAY?")

print("Dog goes woof, cat goes meow.")
print("Bird goes tweet, and mouse goes squeak.")
print("Cow goes moo. Frog goes croak, and the elephant goes toot.")
print("Ducks say quack and fish go blub, and the seal goes" +" OW"*3 +".")
print("But there's one sound that no one knows...")
print(hook)

print()

print("Ring" +" ding"*4 +"eringeding!")

for i in range(2):
    print("Gering"+ " ding"*4 +"eringeding!")
    
print(hook)

for i in range(3):
    print("Wa" +" pa"*5 +" pow!")
