package main

import (
	"fmt"
	"strings"
)

func main() {
	var alphabet [26]int
	for i := 0; i < 26; i++ {
		alphabet[i] = -1
	}

	var S string
	fmt.Scanf("%s", &S)

	for i, v := range strings.Split(S, "") {
		asciiArray := int(v[0]) - 97
		if alphabet[asciiArray] == -1 {
			alphabet[asciiArray] = i
		}
	}

	for i := 0; i < 26; i++ {
		fmt.Printf("%d ", alphabet[i])
	}
}
