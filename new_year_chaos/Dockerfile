FROM golang:1.13
COPY . /app
WORKDIR /app
CMD ["go", "test", "-bench=benchmark_minimum_test.go"]