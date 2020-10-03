package main

import (
	"fmt"
	"testing"
)

func TestMinimumBribes(t *testing.T) {
	var caseOne = []int32{2, 1, 5, 3, 4}
	minimum, chaos := MinimumBribes(caseOne)

	if chaos != "" {
		t.Error(
			fmt.Sprintf(
				"This case should haven't failed.\nGot %d and %s\n",
				minimum,
				chaos,
			),
		)
	}

	if minimum != 3 {
		t.Error("This case expects that the brives are 3")
	}
}

func TestMinimumBribesTwo(t *testing.T) {
	caseTwo := [5]int32{2, 5, 1, 3, 4}
	shifts, chaos := MinimumBribes(caseTwo[:])

	if chaos != ErrorMessage {
		t.Error(
			fmt.Sprintf(
				"This case should have failed.\nGot %d\n",
				shifts,
			),
		)
	}
}

func TestMinimumBribesTcOne(t *testing.T) {
	sample := []int32{5, 1, 2, 3, 7, 8, 6, 4}
	_, chaos := MinimumBribes(sample[:])
	if chaos != ErrorMessage {
		t.Error("This case should have failed")
	}

	sampleTwo := []int32{1, 2, 5, 3, 7, 8, 6, 4}
	shifts, _ := MinimumBribes(sampleTwo[:])
	if shifts != 7 {
		t.Error("I expected 7 shifts")
	}
}

func TestMinimumBribesTcSeven(t *testing.T) {
	var lineScanner LineScanner
	lineScanner.ReadFixture("fixtures/tc6.txt")
	shifts, chaos := MinimumBribes(lineScanner.TestCases[0])
	if chaos != "" {
		t.Error("There should be no error on this case")
	}
	if shifts != 96110 {
		t.Error("I expected 96110")
	}
}
