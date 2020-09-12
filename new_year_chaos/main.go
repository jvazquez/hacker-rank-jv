package main

import "fmt"

func main() {
	queue := [5]int32{2, 1, 5, 3, 4}
	fmt.Printf("All elements: %d\n", queue[0:])
	fmt.Printf("Cap for an array is %d\n", cap(queue))
}
