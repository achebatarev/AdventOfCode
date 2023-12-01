package main

import (
	"challenges/day1"
	"fmt"
	"os"
	"github.com/achebatarev/util"
)

func main() {
	//day1.Run()
	allArgs := os.Args
	fmt.Println(allArgs)
	day = allArgs[1]
	// dict of day as key and function as a value
	part = allArgs[2]
	// execute day1 partA and partB here
	data := util.ReadInput("input.in")
	day1.PartA(data)
		
	//evaluate(day, part) 

}
func evaluateDay(day int, part string) string{
	m := map[string]interface{}{
		"1": day1.RunPartA
	}
	k := 1
	swtich k {
	case 1:

	}
}
func evaluatePart(day int part string) string{
	m := map[string]interface{}{
		"A": day1.RunPartA,
		"B": day1.RunPartA,
	}
	input
}

