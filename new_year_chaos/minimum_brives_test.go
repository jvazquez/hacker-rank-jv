package main

import (
	"fmt"
	"testing"
)

func TestMinimumBribes(t *testing.T) {
	var caseOne = []int32{2, 1, 5, 3, 4}
	var lineScanner LineScanner
	minimum := lineScanner.MinimumBribes(caseOne, false)

	if minimum == ErrorValue {
		t.Error(
			"This case should haven't failed.",
		)
	}

	if minimum != 3 {
		t.Error(fmt.Sprintf("This case expects that the bribes are 3, got %d", minimum))
	}
}

func TestMinimumBribesTcOne(t *testing.T) {
	var lineScanner LineScanner
	var shifts int32
	sample := []int32{5, 1, 2, 3, 7, 8, 6, 4}
	shifts = lineScanner.MinimumBribes(sample[:], false)
	if shifts != ErrorValue {
		t.Error("This case should have failed")
	}

	sampleTwo := []int32{1, 2, 5, 3, 7, 8, 6, 4}
	shifts = lineScanner.MinimumBribes(sampleTwo[:], false)
	if shifts != 7 {
		t.Error(fmt.Sprintf("I expected 7 shifts, got %d", shifts))
	}
}

func TestMinimumBribesTwo(t *testing.T) {
	caseTwo := [5]int32{2, 5, 1, 3, 4}
	var lineScanner LineScanner
	shifts := lineScanner.MinimumBribes(caseTwo[:], false)

	if shifts != ErrorValue {
		t.Error(
			fmt.Sprintf(
				"This case should have failed.\nGot %d\n",
				shifts,
			),
		)
	}
}

func TestMinimumBribesTcSix(t *testing.T) {
	var lineScanner LineScanner
	lineScanner.ReadFixture("fixtures/tc6.txt")
	shifts := lineScanner.MinimumBribes(lineScanner.TestCases[0], false)

	if shifts != 96110 {
		t.Error(fmt.Sprintf("I expected 96110.Got %d\n", shifts))
	}
}

func TestMinimumBribesTcTwo(t *testing.T) {
	var lineScanner LineScanner
	lineScanner.ReadFixture("fixtures/tc2.txt")
	shifts := lineScanner.MinimumBribes(lineScanner.TestCases[0], true)
	if shifts != 966 {
		t.Error(fmt.Sprintf("I expected 966.Got %d\n", shifts))
	}
}
