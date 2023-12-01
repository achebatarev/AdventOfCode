package day1

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"

	"github.com/achebatarev/util"
)

func PartA(I *util.Input) string {
	var line string
	fmt.print
	for I.scanner.Scan() {
		line = I.scanner.Text()
	}
	return line

}
func PartB(I *Input) string {

}
func Run() {
	file, err := os.Open("input.in")
	if err != nil {
		log.Fatal(err)
	}
	var list []int
	group := 0
	result := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if n, err := strconv.Atoi(line); err == nil {
			group += n
		} else {
			list = append(list, group)
			group = 0
		}
		// motherfuck, no builtins for max function for ints
		result = int(math.Max(float64(result), float64(group)))
	}
	list = append(list, group)
	sort.Sort(sort.Reverse(sort.IntSlice(list)))
	result2 := list[0] + list[1] + list[2]
	fmt.Printf("Part 1 %d \n", result)
	fmt.Printf("Part 2 %d \n", result2)
}
