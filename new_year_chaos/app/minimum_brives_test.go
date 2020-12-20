package app

import (
	"fmt"
	"testing"
)

func TestMinimumBribes(t *testing.T) {
	var caseOne = []int32{2, 1, 5, 3, 4}
	minimum := minimumBribesBubbleSort(caseOne)

	if minimum == ErrorValue {
		t.Error(
			"This case should haven't failed.",
		)
	}

	if minimum != 3 {
		t.Error(fmt.Sprintf("This case expects that the bribes are 3, got %d", minimum))
	}
}

func TestMinimumBribesTcZero(t *testing.T) {
	sample := []int32{2, 1, 5, 3, 4}
	shifts := minimumBribesBubbleSort(sample[:])
	if shifts != 3 {
		t.Error("This case should have three positions")
	}

	sample = []int32{2, 5, 1, 3, 4}
	shifts = minimumBribesBubbleSort(sample)

	if shifts != ErrorValue {
		t.Error("This case should be too chaotic")
	}
}

func TestMinimumBribesTcOne(t *testing.T) {
	var shifts int32
	sample := []int32{5, 1, 2, 3, 7, 8, 6, 4}
	shifts = minimumBribesBubbleSort(sample[:])
	if shifts != ErrorValue {
		t.Error("This case should have failed")
	}

	sampleTwo := []int32{1, 2, 5, 3, 7, 8, 6, 4}
	//					 1, 2, 3, 4, 5, 6, 7, 8
	shifts = minimumBribesBubbleSort(sampleTwo[:])
	if shifts != 7 {
		t.Error(fmt.Sprintf("I expected 7 shifts, got %d", shifts))
	}
}

func TestMinimumBribesTwo(t *testing.T) {
	caseTwo := [5]int32{2, 5, 1, 3, 4}
	shifts := minimumBribesBubbleSort(caseTwo[:])

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
	shifts := minimumBribesBubbleSort(lineScanner.TestCases[0])

	if shifts != 96110 {
		t.Error(fmt.Sprintf("I expected 96110.Got %d\n", shifts))
	}
}

func TestMinimumBribesTcTwo(t *testing.T) {
	var lineScanner LineScanner
	lineScanner.ReadFixture("fixtures/tc2.txt")
	shifts := minimumBribesBubbleSort(lineScanner.TestCases[0])
	if shifts != 966 {
		t.Error(fmt.Sprintf("I expected 966.Got %d\n", shifts))
	}
}
