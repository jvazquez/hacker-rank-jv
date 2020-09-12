package main

import (
	"fmt"
	"testing"
)

func TestReverser(t *testing.T) {
	expected := reverser("banana")
	if expected != "ananab" {
		t.Error(fmt.Sprintf("Banana reverse failed! :("))
	}

	expected = reverser("sandía")
	if expected != "aídnas" {
		t.Error(fmt.Sprintf("Sandía reverse failed! :("))
	}
}
