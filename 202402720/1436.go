package main

import (
	"fmt"
	"strings"
)

func available(value int) bool {
	str := fmt.Sprintf("%d", value)

	return strings.Contains(str, "666")
}

func main() {
	var N int
	fmt.Scan(&N)

	count := 1
	value := 666

	for {
		if available(value) {
			if count == N {
				break
			} else {
				count++
			}
		}
		value++
	}

	fmt.Println(value)
}
