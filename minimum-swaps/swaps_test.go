package main

import (
	"github.com/jvazquez/hacker-rank-jv/utils/pkg"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMinimumSwapsDetectsMinimumSwaps(t *testing.T) {
	stubCase := pkg.HackerRankArrayReader("fixtures/input1.txt")
	swaps := MinimumSwaps(stubCase)
	assert.Equal(t, int32(3), swaps)
}
