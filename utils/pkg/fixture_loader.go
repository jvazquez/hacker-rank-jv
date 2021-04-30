package pkg

import (
	"bufio"
	"io"
	"os"
	"strconv"
	"strings"
)

// HackerRankArrayReader used to read the test cases from hacker rank
func HackerRankArrayReader(targetFile string) []int32 {
	fixture, error := os.Open(targetFile)
	defer fixture.Close()
	checkError(error)
	reader := bufio.NewReaderSize(fixture, 1024*1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	n := int32(nTemp)

	arrTemp := strings.Split(readLine(reader), " ")

	var arr []int32

	for i := 0; i < int(n); i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	return arr
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
