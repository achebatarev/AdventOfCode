package util

import (
	"bufio"
	"os"
)

type Input struct {
	scanner *bufio.Scanner
}

func ReadInput(filename string) *Input {
	path := "./day1"
	file, _ := os.Open(path + filename)
	result := Input{
		scanner: bufio.NewScanner(file),
	}
	return *result

}
