package main

const ErrorMessage = "Too chaotic"
const MaxShifts = 2

func main() {
}

func MinimumBribes(consumerLine []int32) (int32, string) {
	var positionShifts int32
	var invalidShift bool
	// fmt.Printf("FS: %v\n", consumerLine)

	for position, person := range consumerLine {

		casesAhead := len(consumerLine[0:position])
		position++
		if person-int32(position) > MaxShifts {
			invalidShift = true
		}

		if casesAhead != 0 {
			// fmt.Printf("%d, Lookahead %v\n", person, consumerLine[0:position])
		}

		for i := 0; i < casesAhead; i++ {
			if consumerLine[i] > person {
				positionShifts += 1
				// fmt.Printf("%d > %d\n", consumerLine[i], person)
			}
		}
	}

	if invalidShift {
		return 0, ErrorMessage
	} else {
		return positionShifts, ""
	}
}
