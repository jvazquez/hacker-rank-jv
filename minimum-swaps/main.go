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

// minimumSwaps finds the minimum number of swaps required to sort the
// array in ascending order.
func minimumSwaps(arr []int32) int32 {
	return 0
}
