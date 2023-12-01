module github.com/achebatarev/aoc2022

go 1.19

replace challenges/day1 => ./challenges/day1

require (
	challenges/day1 v0.0.0-00010101000000-000000000000
	github.com/achebatarev/util v0.0.0-00010101000000-000000000000
)

replace github.com/achebatarev/util => ./util
