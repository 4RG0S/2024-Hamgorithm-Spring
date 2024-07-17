package main

import (
	"fmt"
	"strings"
)

func main() {
	var n [5][15]string

	for i := 0; i < 5; i++ {
		var input string
		fmt.Scanf("%s", &input)

		for j, c := range strings.Split(input, "") {
			n[i][j] = c
		}
	}

	for i := 0; i < 15; i++ {
		for j := 0; j < 5; j++ {
			fmt.Print(n[j][i])
		}
	}
}
