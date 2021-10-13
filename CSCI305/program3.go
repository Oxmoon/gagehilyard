package main
import (
	"fmt"
	"os"
	"regexp"
	"strings"
	"strconv"
)
/* This program takes a text file and parses all integers seperated by other
 * characters, treating them as ASCII, code and outputs a decoded message
 */

// Error checking function
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// File reading function, returns string
func infile(fname string) string {
	data, err := os.ReadFile(fname)
	check(err)
	return string(data)
}

// Takes string of data from a file and converts it to a decoded string
func decode(data string) string {
	//cleans up code
	reg, err := regexp.Compile("[^0-9]+")
	check(err)
	cleanString := reg.ReplaceAllString(data, " ")

	//splices string
	splice := strings.Fields(cleanString)
	stringLength := len(splice)
	resultString := make([]string, stringLength) //to be the output

	//changes ASCII code to string
	for i := 0; i < stringLength; i++ {
		letter, err := strconv.Atoi(splice[i])
		check(err)
		newletter := int32(letter)
		resultString[i] = string(newletter)
	}
	finalString := strings.Join(resultString, " ")
	return finalString
}

//Writes new data (secret clue), from string array
func writeMessage(str string, name string) {
	file, err := os.Create("decoded_" + name)
	check(err)
	defer file.Close()

	_,err2 := file.WriteString(str +"\n")
	check(err2)

	fmt.Println("Done!")
}

func main() {
	// Asks for name of file
	fmt.Println("Enter name of file with .txt extension.")
	var fname string
	fmt.Scanln(&fname)

	//Reads file and decodes
	f := infile(fname)
	decodedString := decode(f)

	//Outputs file with name attached
	writeMessage(decodedString, fname)
}
