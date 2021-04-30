package main

import (
	"github.com/jvazquez/hacker-rank-jv/utils/pkg"
	"log"
)

func main() {
	var testCase []int32
	testCase = pkg.HackerRankArrayReader("fixtures/input1.txt")
	log.Printf("%v", testCase)
}
