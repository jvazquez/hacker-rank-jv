package main

import (
	"bufio"
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

func (lp *LineScanner) MinimumBribes(consumerLine []int32) int32 {
	var positionShifts, currentFixedPosition int32
	log.Println(consumerLine)
	for currentPosition, currentPerson := range consumerLine {
		//currentFixedPosition = int32(currentPosition) + 1
		currentFixedPosition = int32(currentPosition)

		if (currentPerson-currentFixedPosition)-1 > MaxShifts {
			return ErrorValue
		}

		/*
			Avoid the full count from currentFixedPosition to 0.
			I just need to count from currentFixedPosition, one head
		*/
		twoPositionsBefore := lp.Max(currentFixedPosition+2, 0)
		myPositions := consumerLine[currentFixedPosition:twoPositionsBefore]
		log.Print(myPositions)
		/*
			for j:= 2 ; j > 0; j-- {
				if consumerLine[currentFixedPosition + int32(j)] < currentPerson {
					positionShifts += 1
				}
			}
		*/
		/*
			for _, personBefore := range myPositions {
				if againstVersion(currentPerson, personBefore) {
					positionShifts += 1
				}
			}
		*/
	}

	return positionShifts
}

func againstVersion(person int32, previousPerson int32) bool {
	log.Printf("%d > %d = %t", previousPerson, person, previousPerson > person)
	return previousPerson > person
}

func firstWorkingCheck(person int32, position int32) bool {
	return position > person
}

func personIsAheadOfCurrentPosition(person int32, position int32) bool {
	log.Printf("%d - %d %d", person, position, person-position)
	return (person - position) > 2
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
