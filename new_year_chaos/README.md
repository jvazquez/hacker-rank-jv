Url: [New year chaos](https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays)

The issue with our solution in Golang, is that
the bubblesort works perfect, but with test cases
6, 7, 8 and 9 we fail because

```
Time limit exceeded
Your code did not execute within the time limits. Please optimize your code. For more information on execution time limits, refer to the environment page
```

So that is why we've got a Dockerfile.
To simulate hackerrank environment, build with makefile

`make profile_image` to build the image
`make run_profile_test` to run the profile of the test cases