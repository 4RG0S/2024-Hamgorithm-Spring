package main

import (
	"fmt"
)

var (
	gradeMap = map[string]float32{
		"A+": 4.5,
		"A0": 4.0,
		"B+": 3.5,
		"B0": 3.0,
		"C+": 2.5,
		"C0": 2.0,
		"D+": 1.5,
		"D0": 1.0,
		"F":  0.0,
	}
)

func main() {
	var totalCredit float32
	var totalScore float32

	for i := 0; i < 20; i++ {
		var input string
		var credit float32
		var grade string

		fmt.Scanf("%s %f %s", &input, &credit, &grade)

		if grade != "P" {
			totalCredit += float32(credit)
			totalScore += float32(credit) * gradeMap[grade]
		}
	}

	fmt.Printf("%.6f\n", totalScore/totalCredit)
}
