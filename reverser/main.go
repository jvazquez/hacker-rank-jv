package main

import (
	"fmt"
	reverser "reverser/pkg"
)

func main() {
	var word = "Banana"
	fmt.Printf("%s reversed is %s\n", word, reverser.Reverse(word))
}
