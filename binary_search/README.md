binary search

log2(n) + 1 is the formula that we use to calculate the worst
case scenario of searches in a sorted array.

We use + 1 because that final guess is what it means that we
either find a value or not.

Using binary search, we cut in half the values 
and reduce the time of guesses.

using a linear search of an array of n elements, it will
take len(array) 