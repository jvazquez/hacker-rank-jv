package main

import (
	"bufio"
	"io"
	"os"
	"strconv"
	"strings"
)

const ErrorMessage = "Too chaotic"
const MaxShifts = 2

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

func MinimumBribes(consumerLine []int32) (int32, string) {
	var positionShifts int32
	var invalidShift bool

	for position, person := range consumerLine {
		casesAhead := len(consumerLine[0:position])
		position++
		if person-int32(position) > MaxShifts {
			invalidShift = true
		}

		for i := 0; i < casesAhead; i++ {
			if consumerLine[i] > person {
				positionShifts += 1
			}
		}
	}

	if invalidShift {
		return 0, ErrorMessage
	} else {
		return positionShifts, ""
	}
}
