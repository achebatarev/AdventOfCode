package main

import (
	"bufio"
	"cast"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const root = "./"

type Interval struct {
	l int
	r int
}

func parseData(data []string) [][2]Interval {
	var result [][2]Interval
	for _, line := range data {
		ans := [2]Interval{}
		res := strings.Split(line, ",")

		x1 := strings.Split(res[0], "-")
		l1 := cast.ToInt(x1[0])
		r1, _ := strconv.Atoi(x1[1])
		ans[0] = Interval{l1, r1}

		x2 := strings.Split(res[1], "-")
		l2, _ := strconv.Atoi(x2[0])
		r2, _ := strconv.Atoi(x2[1])
		ans[1] = Interval{l2, r2}

		result = append(result, ans)
	}
	return result
}

func partA(data [][2]Interval) int {
	//fmt.Println(data)
	var result int
	for _, intervals := range data {
		i1 := intervals[0]
		i2 := intervals[1]
		if i1.l <= i2.l && i1.r >= i2.r {
			result += 1
		} else if i2.l <= i1.l && i2.r >= i1.r {
			result += 1
		}
	}

	return result
}
func partB(data [][2]Interval) int {
	var result int
	for _, intervals := range data {
		i1 := intervals[0]
		i2 := intervals[1]
		if i1.l <= i2.l && i1.r >= i2.l {
			result += 1
		} else if i2.l <= i1.l && i2.r >= i1.l {
			result += 1
		}
	}

	return result
}

func main() {
	filename := "test.in"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}
	data1 := readInput(filename)
	data := parseData(data1)
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
