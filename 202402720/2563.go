package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)

	var tile [100][100]int

	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			tile[i][j] = 0
		}
	}

	for i := 0; i < N; i++ {
		var x, y int
		fmt.Scanf("%d %d", &x, &y)
		for j := x; j < x+10; j++ {
			for k := y; k < y+10; k++ {
				tile[j][k] = 1
			}
		}
	}

	var count int
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			if tile[i][j] == 1 {
				count++
			}
		}
	}

	fmt.Println(count)
}
