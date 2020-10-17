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

func (lp LineScanner) Max(maxValue int32, minValue int32) int32 {
	if maxValue < minValue {
		return minValue
	} else {
		return maxValue
	}
}

func (lp *LineScanner) MinimumBribes(consumerLine []int32, verbose bool) int32 {
	var positionShifts, currentFixedPosition int32
	logMessage(fmt.Sprintf("%d", consumerLine), verbose)

	for currentPosition, currentPerson := range consumerLine {
		currentFixedPosition = int32(currentPosition) + 1
		if (currentPerson - currentFixedPosition) > MaxShifts {
			return ErrorValue
		}

		//logMessage(fmt.Sprintf("%d - %d = %d", currentFixedPosition, currentPerson, manualDelta), verbose)
		manualDelta := currentFixedPosition - currentPerson
		switch {
		case manualDelta > 1:
			positionShifts += manualDelta
		//case manualDelta < 1:
		//	logMessage(fmt.Sprintf("+ %d", manualDelta * -1), verbose)
		//	positionShifts += manualDelta * -1
		default:
			deltaIndex := lp.Max(currentFixedPosition-3, 0)
			lineAhead := consumerLine[deltaIndex : currentFixedPosition-1]
			logMessage(fmt.Sprintf("[%d:%d] ==> %d <== Pivot %d",
				deltaIndex, currentFixedPosition-1, lineAhead, currentPerson),
				verbose)
			sliceAhead(lineAhead, currentPerson, &positionShifts, verbose)
		}

		logMessage(fmt.Sprintf("positionShift: %d", positionShifts), verbose)
	}

	return positionShifts
}

func logMessage(message string, show bool) {
	if show {
		log.Println(message)
	}
}

func sliceAhead(lineAhead []int32, currentPerson int32, positionShifts *int32, verbose bool) {
	for _, personAhead := range lineAhead {
		if personAhead > currentPerson {
			logMessage(fmt.Sprintf("%d > %d = %t", personAhead,
				currentPerson, personAhead > currentPerson),
				verbose,
			)
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
