package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
var scanner *bufio.Scanner = bufio.NewScanner(os.Stdin)

func main() {
	defer writer.Flush()

	var N int
	fmt.Fscanln(reader, &N)

	arr := make([]int, N)

	for i := 0; i < N; i++ {
		fmt.Fscanln(reader, &arr[i])
	}

	sort.Ints(arr)

	for i := 0; i < N; i++ {
		fmt.Fprintln(writer, arr[i])
	}
}
