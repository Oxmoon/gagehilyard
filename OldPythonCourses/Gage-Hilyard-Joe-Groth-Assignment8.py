# -----------------------------------------
# Gage Hilyard, Joe Groth           
# CSCI 107, Assignment 8                   
# Last Updated: November 16, 2018                         
# -----------------------------------------
# Make modifications to a musical          
# composition program.                     
# -----------------------------------------

import pyaudio     # Remember to install pyaudo or this will not work
import math
import struct

# beats per minute
# ----- NOTE!!! -----------------
# Change BPM to 520 for our song
# -------------------------------
BPM = 520

# allowed notes and their frequencies
# NOTE
# Notes with '1' is an octave higher
FREQUENCIES = {'A': 440, 'A#': 466, 'B': 493,
               'C': 523, 'C#': 554, 'D': 587,
               'D#': 622, 'E': 659, 'F': 698,
               'F#': 740, 'G': 784, 'G#': 830,
               'a': 433, 'a#': 463, 'b': 493,
               'c': 523, 'c#': 554, 'd': 587,
               'd#': 622, 'e': 659, 'f': 698,
               'f#': 740, 'g': 784, 'g#': 830, 'rest': 000,
               'A1':880, 'A1#': 932, 'B1': 988,
               'C1': 1047, 'C1#': 1109, 'D1': 1175,
               'D1#':1245, 'E1':1319, 'F1':1397, 'F1#':1480,
               'G1':1568,'a1':880, 'a1#': 932, 'b1': 988,
               'c1': 1047, 'c1#': 1109, 'd1': 1175,
               'd1#':1245, 'e1':1319, 'f1':1397,'f1#':1480,
               'g1':1568,
               }

# the possible musical notes
POSSIBLE_NOTES = ['A','a', 'A#','a#', 'B','b', 'C','c', 'C#', 'c#','D','d', 'D#',
                  'd#', 'E','e', 'F','f','F#','f#', 'G','g', 'G#','g#','rest',
                  'A1', 'a1', 'A1#', 'a1#', 'B1', 'b1', 'C1', 'c1', 'C1#', 'c1#',
                  'D1', 'd1', 'D1#', 'd1#','E1','e1','F1','f1','F1#','f1#','G1','g1']

# -------------------------------------------------

def view_song(song):
    
    if len(song) == 0:
        print("No song data to display.")
        
    else:
        # print the header row
        for note in POSSIBLE_NOTES:
            print("{:4s}".format(note), end="")
        print()
        
        for note in song:
            note_name = note[0]     # note name
            note_length = note[1]   # note length

            # now print this line of the score
            for bar in range(note_length):
                for note in POSSIBLE_NOTES:
                    if note == note_name:
                        print("{:4s}".format("*"), end="")
                    else:
                        print("{:4s}".format("-"), end="")
                print()

# -------------------------------------------------

def compose_song():

    # create a list of tuples of (note, length) that is the song and return it

    list_of_notes = []
    new_note = "NOT DONE"

    while new_note != "DONE":
        
        new_note = input("What note would you like to play (or type 'DONE' if finished) ?: ")

        if new_note != 'DONE':
            if new_note in POSSIBLE_NOTES:                  # valid note?
                new_length = int(input("What is the length of this note?: "))
                if (new_length > 0) and (new_length <= 4):  # valid note length?
                    note_tuple = (new_note, new_length)     # form a tuple
                    list_of_notes.append(note_tuple)
                else:
                    print("Invalid note length.  Please try again.")
            else:
                print("Invalid note.  Please try again.")

    return list_of_notes

# -------------------------------------------------

def play_song(song):

    if len(song) == 0:
        print("Invalid song, contains no notes!")
    else:
        # sample rate
        sample_rate = 44100
        bar_length = 60 / BPM

        # create the audio device and open the audio stream
        # fp precision is default, 1 channel (mono) audio
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=1)

        # create a stream to add things to
        current_stream = []
        
        for i in song:

            # get the note name and note length
            note = i[0]
            note_frequency = FREQUENCIES[note]
            note_length = float(i[1])

            for i in range(0, int(note_length * bar_length * sample_rate)):

                # sine calculation for the current instrument
                sample = (1.0 * math.pi * note_frequency * i) / sample_rate

                # a sine wave is the current instrument
                current_note = math.sin(sample)

                # append the value to teh stream
                current_stream.append(current_note)

            # append some silence so we don't get a bad pop
            for i in range(1, 1000):
                current_stream.append(0.0)

        # write data to the stream
        # once finished, then write all data to the stream buffer (a special pack routine to implement the buffer as a list)
        stream.write(struct.pack('f'*len(current_stream), *current_stream))

        # finish by closing the stream and term the object
        print("Done playing!")
        stream.close()
        p.terminate()

# --------------------------------------------------------------------------------------------------------

def change_bpm():
    global BPM
    counter = 0
    print("BPM:",BPM)
    while counter != 1:
        value = int(input("Enter a BPM from 60 to 200: "))
        if value < 60:
            print("Invalid option, please try again. ")
        elif value > 200:
            print("Invalid option, please try again. ")
        else:
            BPM = value
            counter = 1
        
    

# -------------------------------------------------

def main():

    print("Welcome to TunePlayer!")
    my_epic_song = []           # a place to store the tune
    selection = "0"             # initialize the user's selection
    
    while selection != "6":

        # menu items
        print("Some options are...")
        print("1. Create a tune.")
        print("2. View tune.")
        print("3. Play a tune.")
        print("4. Erase the tune and start over.")
        print("5. Change BPM.")
        print("6. Exit. ")

        # make a selection
        selection = input("What would you like to do?: ")

        # choose between the menu items
        if selection == "1":
            # create a composition with the score editor
            my_epic_song = compose_song()
        elif selection == "2":
            # view the score
            view_song(my_epic_song)
        elif selection == "3":
            # play the song that I've written
            play_song(my_epic_song)
        elif selection == "4":
            # replace the song with a blank array
            my_epic_song = []
        elif selection == "5":
            change_bpm()
            # changes BPM
        elif selection == "6":
            # exit the menu
            pass
        else:
            # a poor choice
            print("The selection was invalid, please try again...")

    # we're done here
    print("Goodbye!")

# -------------------------------------------------

# start the music program
main()

# Guile's Theme from Street Fighter
# BPM should be set at 520 for best result

my_epic_song = [('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 1), ('d', 2), ('d#', 1), ('rest', 1), ('d',1), ('f', 1),('rest',1),('f',1),
                ('d#', 2), ('d', 2), ('a#', 2), ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 1), ('d', 2), ('d#', 1), ('rest', 1), ('d',1), ('f', 1),('rest',1),('f',1),
                ('d#', 2), ('d', 2), ('a#', 2),
                ('c',8),('d',2),('d#',1),('f',3),('g',3),('g',1),('f',2),('a1#',4),('g#',2),('g',1),
                ('g#',2),('d',3),('d#',1),('d#',2),('f',2),('rest',2),('a#',2),('d',2),('d#',2),('g#',3),('a1#',3),('g',2),('rest',1),
                ('g',1),('f',1),('d',3),
                ('c',8),('d',2),('d#',1),('f',3),('g',3),('g',1),('g#',2),('f',2),('rest',1),('f',1),
                ('g',1),('g#',3),('a1#',5),('c1',2),('d1',1),('d1#',3),('g1',2),('f1',2),('d1',2),
                ('a1#',2),('c1',6),('d1',2),('d1#',2),('f1',2),('c1',6),('d1',2),('d1#',2),('f1',2),('g1',8),
                ('rest', 4),
                ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 1), ('d', 2), ('d#', 1), ('rest', 1), ('d',1), ('f', 1),('rest',1),('f',1),
                ('d#', 2), ('d', 2), ('a#', 2), ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 2), ('d#', 1), ('d', 1), ('rest', 1), ('d',1), ('d#', 3),('rest',1),('d',1),
                ('d#', 1), ('d', 2), ('d#', 1), ('rest', 1), ('d',1), ('f', 1),('rest',1),('f',1),
                ('d#', 2), ('d', 2), ('a#', 2)]
play_song(my_epic_song)

