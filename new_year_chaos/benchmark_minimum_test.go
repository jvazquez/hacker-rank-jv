package main

import (
	"testing"
)

func BenchmarkMinimumBribes(b *testing.B) {
	var lineScanner LineScanner
	lineScanner.ReadFixture("fixtures/tc6.txt")
	for i := 0; i < b.N; i++ {
		_ = lineScanner.MinimumBribes(lineScanner.TestCases[0], false)
	}

}
