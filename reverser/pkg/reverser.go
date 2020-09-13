package reverser

import (
	"log"
	"unicode/utf8"
)

func Reverse(toReverse string) string {
	var stringLength int

	stringLength = utf8.RuneCountInString(toReverse)

	log.Printf("We received a string (%s) that is %d chars long (RuneCount)\n"+
		"and is %d bytes long (len)",
		toReverse,
		utf8.RuneCountInString(toReverse),
		len(toReverse),
	)
	// Create a slice of bytes of n chars
	runeSlice := make([]rune, utf8.RuneCountInString(toReverse))
	log.Printf("We have a slice that is %d bytes long\n", len(runeSlice))

	for _, character := range toReverse {
		stringLength--
		runeSlice[stringLength] = character
	}

	log.Printf("%s runeSlice is %s", toReverse, string(runeSlice))
	return string(runeSlice)
}
