package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

const MaxShifts = 2
const ErrorValue = -1

type LineScanner struct {
	TestCases    map[int][]int32
	TestCasePath string
}

func (lp LineScanner) GetPeopleLine(peopleInLine int, lineOfPeople []string) []int32 {
	var peopleLine []int32
	for i := 0; i < peopleInLine; i++ {
		qItemTemp, err := strconv.ParseInt(lineOfPeople[i], 10, 64)
		checkError(err)
		person := int32(qItemTemp)
		peopleLine = append(peopleLine, person)
	}
	return peopleLine
}

func (lp *LineScanner) ReadFixture(testCasePath string) {
	var peopleInLine int
	fixture, error := os.Open(testCasePath)
	defer fixture.Close()
	checkError(error)
	reader := bufio.NewReaderSize(fixture, 1024*1024)
	tTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	fixtureLines := int32(tTemp)
	lp.TestCases = make(map[int][]int32)
	for tItr := 0; tItr < int(fixtureLines); tItr++ {
		literalPeopleInLine, err := strconv.ParseInt(readLine(reader), 10, 64)
		checkError(err)
		lineOfPeople := strings.Split(readLine(reader), " ")
		peopleInLine = int(literalPeopleInLine)
		lp.TestCases[tItr] = lp.GetPeopleLine(peopleInLine, lineOfPeople)
	}
}

func max(valueA int32, valueB int32) int32 {
	if valueA < valueB {
		return valueB
	} else {
		return valueA
	}
}

func (lp *LineScanner) MinimumBribes(consumerLine []int32) int32 {
	var positionShifts, currentFixedPosition int32

	for currentPosition, currentPerson := range consumerLine {
		currentFixedPosition = int32(currentPosition) + 1
		manualDelta := currentFixedPosition - currentPerson
		if manualDelta > MaxShifts {
			return ErrorValue
		}

		switch {
		case manualDelta > 1:
			positionShifts += manualDelta
		default:
			deltaIndex := max(currentFixedPosition-3, 0)
			lineAhead := consumerLine[deltaIndex : currentFixedPosition-1]
			viewTwoPositionsAhead(lineAhead, currentPerson, &positionShifts)
		}
	}

	return positionShifts
}

func minimumBribes(consumerLine []int32) int32 {
	var positionShifts, currentFixedPosition int32
	fmt.Println(consumerLine)
	for currentPosition, currentPerson := range consumerLine {
		currentFixedPosition = int32(currentPosition) + 1
		positionDifference := currentPerson - currentFixedPosition

		if positionDifference > MaxShifts {
			return ErrorValue
		}
		twoPositionsAheadFromHere := max(int32(currentPosition-2), 0)
		lineAhead := consumerLine[twoPositionsAheadFromHere:currentPosition]
		for _, personAhead := range lineAhead {
			if currentPerson < personAhead {
				positionShifts = positionShifts + 1
				log.Printf("%d < %d => +%d\n", currentPerson, personAhead, positionShifts)
			}
		}
		/*else  if positionDifference > 0 {
			positionShifts += positionDifference
		} else if positionDifference < 0 {
			twoPositionsAheadFromHere := max(int32(currentPosition - 2), 0)
			lineAhead := consumerLine[twoPositionsAheadFromHere : currentPosition]
			for _, personAhead := range lineAhead {
				if personAhead > currentPerson {
					positionShifts = positionShifts + 1
				}
			}
		}
		*/
	}
	return positionShifts
}

func viewTwoPositionsAhead(lineAhead []int32, currentPerson int32, positionShifts *int32) {
	for _, personAhead := range lineAhead {
		if personAhead > currentPerson {
			*positionShifts += 1
		}
	}
}

func main() {

}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
