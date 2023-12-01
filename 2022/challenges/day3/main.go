package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

const root = "./"

func findPriority(char rune) int {
	if unicode.IsLower(char) {
		return int('a') + 1
	} else {
		return (int(char) - int('A')) + 27
	}
}
func partA(data []string) int {
	var result int
	for _, s := range data {
		d := make(map[rune]bool)
		mid := len(s) / 2
		for _, e := range s[:mid] {
			d[e] = true
		}
		for _, e := range s[mid:] {
			if d[e] {
				result += findPriority(e)
				break
			}
		}
	}
	return result
}

func findCommon(d map[rune]bool) rune {
	common := 'a'
	for k, v := range d {
		if v {
			common = k
		}
	}
	return common
}
func partB(data []string) int {
	var result int
	d := make(map[rune]bool)
	for i, s := range data {
		intersection := make(map[rune]bool)
		if (i != 0) && (i%3 == 0) {
			common := findCommon(d)
			d = make(map[rune]bool)
			result += findPriority(common)
		}
		for _, char := range s {
			if i%3 == 0 || d[char] {
				intersection[char] = true
			}
		}
		d = intersection
	}
	common := findCommon(d)
	//fmt.Printf("%q\n", common)
	result += findPriority(common)
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
