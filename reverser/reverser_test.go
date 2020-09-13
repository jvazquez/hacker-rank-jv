package main

import (
	"fmt"
	reverser "reverser/pkg"
	"testing"
)

func TestReverser(t *testing.T) {
	expected := reverser.Reverse("banana")
	if expected != "ananab" {
		t.Error(fmt.Sprintf("Banana reverse failed! :("))
	}

	expected = reverser.Reverse("sandía")
	if expected != "aídnas" {
		t.Error(fmt.Sprintf("Sandía reverse failed! :("))
	}
}
