package main

import (
	"fmt"
	"log"
	"strings"
	"unicode/utf8"
)

func reverser(toReverse string) string {
	reversed := make([]string, utf8.RuneCountInString(toReverse))
	i := len(toReverse)

	for _, c := range toReverse {
		i--
		reversed[i] = string(c)
	}

	log.Printf("%s reversed is %s", toReverse, reversed)

	return strings.Join(reversed, "")
}

func main() {
	var word = "Banana"
	fmt.Printf("%s reversed is %s\n", word, reverser(word))
}
