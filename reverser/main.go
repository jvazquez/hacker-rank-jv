package main

import "fmt"

type UserInput struct {
	Word string
}

func(u *UserInput) reverser() string {
	wordlen := len(u.Word)
	var reversed [wordlen]str

	for i := wordlen; i >= 0; i-- {
		reversed[i] = u.Word[i]
	}
}

func main(){
	userData := UserInput{Word: "Banana"}
	wordlen := len(userData.Word) - 1

	for i := wordlen; i >= 0; i-- {
		fmt.Printf("%c", userData.Word[i])
	}
}