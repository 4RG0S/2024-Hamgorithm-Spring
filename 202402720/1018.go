package main

import (
	"fmt"
	"strings"
)

var (
	tile [][]string

	firstWTile = [][]string{
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
	}

	firstBTile = [][]string{
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
		{"B", "W", "B", "W", "B", "W", "B", "W"},
		{"W", "B", "W", "B", "W", "B", "W", "B"},
	}
)

func getRemaningCount(x int, y int) int {
	var firstCount int
	var secondCount int

	for i := x; i < x+8; i++ {
		for j := y; j < y+8; j++ {
			if tile[i][j] != firstWTile[i-x][j-y] {
				firstCount++
			}
			if tile[i][j] != firstBTile[i-x][j-y] {
				secondCount++
			}
		}
	}

	if firstCount < secondCount {
		return firstCount
	} else {
		return secondCount
	}
}

func main() {
	var N, M int
	fmt.Scan(&N, &M)

	tile = make([][]string, N)
	for i := range tile {
		tile[i] = make([]string, M)
	}

	for i := 0; i < N; i++ {
		var input string
		fmt.Scan(&input)

		for j, v := range strings.Split(input, "") {
			tile[i][j] = v
		}
	}

	min := 1 << 31

	for i := 0; i <= N-8; i++ {
		for j := 0; j <= M-8; j++ {
			v := getRemaningCount(i, j)
			if v < min {
				min = v
			}
		}
	}

	fmt.Println(min)
}
