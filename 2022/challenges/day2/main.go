package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const root = "./"

func partA(data []string) int {
	result := 0
	for _, e := range data {
		res := strings.Split(e, " ")
		you := res[0]
		me := res[1]
		result += int(rune(me))

	}
	return result
}

func partB(data []string) int {
	result := 0
	for _, e := range data {
		res := strings.Split(e, " ")
		you := res[0]
		me := res[1]
		switch me {
		case "X": //lose
			result += 0
			if you == "A" {
				result += 3
			} else if you == "B" {
				result += 1
			} else {
				result += 2
			}
		case "Y": // draw
			result += 3
			if you == "A" { //rock
				result += 1
			} else if you == "B" {
				result += 2
			} else {
				result += 3
			}
		case "Z": //win
			result += 6
			if you == "A" {
				result += 2
			} else if you == "B" {
				result += 3
			} else {
				result += 1
			}

		}
	}
	return result
}
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
