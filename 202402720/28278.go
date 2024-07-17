package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var scanner *bufio.Scanner = bufio.NewScanner(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	var N int
	s := make([]int, 1000000)
	top := 0

	fmt.Scanln(&N)

	for i := 0; i < N; i++ {
		scanner.Scan()
		input := scanner.Text()
		args := strings.Split(input, " ")

		switch args[0] {
		case "1":
			s[top], _ = strconv.Atoi(args[1])
			top += 1
		case "2":
			if top == 0 {
				fmt.Fprintln(writer, "-1")
			} else {
				fmt.Fprintln(writer, s[top-1])
				s[top-1] = 0
				top -= 1
			}
		case "3":
			fmt.Fprintln(writer, top)
		case "4":
			if top == 0 {
				fmt.Fprintln(writer, "1")
			} else {
				fmt.Fprintln(writer, "0")
			}
		case "5":
			if top == 0 {
				fmt.Fprintln(writer, "-1")
			} else {
				fmt.Fprintln(writer, s[top-1])
			}
		}
	}
}
