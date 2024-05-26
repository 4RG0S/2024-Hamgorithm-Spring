package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)

	for i := 1; i <= 9; i++ {
		fmt.Printf("%d * %d = %d\n", N, i, N*i)
	}
}
