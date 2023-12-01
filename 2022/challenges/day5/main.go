package main

import (
	"bufio"
	"fmt"
	"os"
)

const root = "./"

func partA(data []string) int {

}
func partB(data []string) int {}

func main() {
	filename := "test.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}
	data := readInput(filename)
	fmt.Println(partA(data))
	fmt.Println(partB(data))
}

func readInput(filename string) []string {
	file, _ := os.Open(root + filename)
	var list []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		list = append(list, scanner.Text())
	}
	return list
}
