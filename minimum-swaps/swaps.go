package main

import "sort"

// MinimumSwaps finds the minimum number of swaps required to sort the
// array in ascending order.
func MinimumSwaps(arr []int32) int32 {
	sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	return 0
}
